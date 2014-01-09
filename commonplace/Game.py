"""
Jonathan Reem
January 2013

Implements the Game class, which contains a full, playable game as well as the
playgame and playturn methods.
"""

from random import random
from time import sleep
from operator import contains

from commonplace.Exceptions import (BaseVictoryException,
                                    BaseDefeatException,
                                    MonsterDeadException,
                                    AbortFightException,
                                    UnhandledOptionError,
                                    PlayerDeadException,
                                    FinalBossDeadException)

from commonplace.Base import (format_objects,
                              spaced_print,
                              BaseObj,
                              bumped_range,
                              assert_with_dump)

from commonplace.Items import BaseEquipment, BaseTreasure
from commonplace.Rooms import BrainRoom, PoemRoom

# Unfortunately I don't have time to actually fix this
# right now. I might later.
# pylint: disable=R0912, R0915, R0201


class PoemGame(BaseObj):

    """Game Object that takes a map and player and runs the game."""

    def __init__(self, name, description, game_map, player):
        BaseObj.__init__(self, name, description)
        self.game_map = game_map
        self.player = player
        self.current_room = self.game_map.start_room
        self.turn_count = 0

    def play_game(self):
        "Plays the entire game."
        print "Welcome to the game of {0.name}.\n\n{0.description}\n".format(
            self)
        spaced_print("You begin your adventure in {0.name}.".format(
            self.current_room))

        while True:
            try:
                self.play_turn()
            except BaseDefeatException as defeat:
                self.end_game_defeat(defeat)
                break
            except BaseVictoryException as victory:
                self.end_game_victory(victory)
                break

    def play_turn(self):
        "Plays a turn of the game."
        self.turn_count += 1
        print "Turn {0.turn_count}:\n".format(self)

        self.player.health += self.player.max_health / 5

        spaced_print("Location:", pre=False)
        print self.current_room.full_info()

        while True:
            main_choice = prompt(self.current_room.valid_options + ['player'])
            # Valid options are:
            #    doors -- poem and regular
            #    items -- regular
            #    monsters -- regular
            #    player -- poem and regular
            #    treasure -- poem
            #    guardian -- poem
            #    charactercs -- regular, but not included.

            # Could be better implemented with a callback pattern but there are
            # time constraints here.
            if main_choice == 'doors':
                spaced_print(format_objects(self.current_room.doors))
                door_choice = prompt(self.current_room.doors.keys() + ['back'])

                if door_choice == 'back':
                    continue

                self.current_room = self.current_room.doors[door_choice]
                break

            elif main_choice == 'items':
                assert_with_dump(self.current_room, BrainRoom,
                                 callback=isinstance)

                spaced_print(format_objects(self.current_room.items))
                item_choice = prompt(
                    bumped_range(len(self.current_room.items)) + ['back'])

                if item_choice == 'back':
                    continue

                item_index = int(item_choice) - 1
                current_item = self.current_room.items[item_index]

                spaced_print(str(current_item))
                item_action = prompt(['info', 'take', 'back'])

                if item_action == 'back':
                    continue
                elif item_action == 'take':
                    self.player.inventory.append(
                        self.current_room.items.pop(item_index))
                    continue
                elif item_action == 'info':
                    spaced_print(current_item.full_info())
                    continue

            elif main_choice == 'player':
                spaced_print(self.player.full_info())
                player_choice = prompt(["inventory", "back"])

                if player_choice == 'back':
                    continue
                elif player_choice == 'inventory':
                    spaced_print("Inventory:\n{}".format(format_objects(
                        self.player.inventory)))
                    inventory_choice = prompt([str(i)
                                               for i in bumped_range(
                                                   len(self.player.inventory))
                                               ] + ['back'])

                    if inventory_choice == 'back':
                        continue

                    inventory_choice = int(inventory_choice) - 1
                    if inventory_choice in range(len(self.player.inventory)):

                        inventory_item = self.player.inventory[
                            inventory_choice]
                        if isinstance(inventory_item, BaseEquipment):
                            spaced_print(inventory_item.full_info())
                            item_choice = prompt(['equip', 'back'])

                            if item_choice == 'back':
                                continue
                            elif item_choice == 'equip':
                                assert_with_dump(self.player.equipped,
                                                 inventory_item.eq_type,
                                                 callback=contains)
                                self.player.equip(inventory_item,
                                                  inventory_item.eq_type)

                        elif isinstance(inventory_item, BaseTreasure):
                            spaced_print(inventory_item.full_info())
                            treasure_choice = prompt(['back'])

                            if treasure_choice == 'back':
                                continue

            elif main_choice == 'monsters':
                assert_with_dump(self.current_room, BrainRoom,
                                 callback=isinstance)

                spaced_print("Monsters:\n{}".format(
                    format_objects(self.current_room.monsters)))
                monster_choice = prompt([str(i)
                                         for i in bumped_range(len(
                                             self.current_room.monsters))] \
                                        + ['back'])

                if monster_choice == 'back':
                    continue

                monster_index = int(monster_choice) - 1
                if monster_index in range(len(
                        self.current_room.monsters)):

                    current_monster = self.current_room.monsters[monster_index]
                    spaced_print(current_monster.full_info())
                    monster_action = prompt(['attack', 'back'])

                    if monster_action == 'back':
                        continue
                    else:
                        try:
                            fight(self.player, current_monster)
                        except MonsterDeadException:
                            spaced_print("The monster dropped:\n\n{}".format(
                                current_monster.drop))
                            self.player.inventory.append(current_monster.drop)
                            del self.current_room.monsters[monster_index]
                        except AbortFightException:
                            spaced_print("You escaped.")

            elif main_choice == 'guardian':
                assert_with_dump(self.current_room, PoemRoom,
                                 callback=isinstance)

                spaced_print("Guardian:\n{}".format(
                    str(self.current_room.guardian)))
                spaced_print("You cannot run from a guardian. You must fight.",
                             pre=False)

                sleep(0.3)

                try:
                    fight(self.player, self.current_room.guardian,
                          monster_name='guardian', can_run=False)
                except MonsterDeadException:
                    if self.current_room.guardian.monster_type == 'FinalBoss':
                        raise FinalBossDeadException

                    spaced_print("The guardian dropped:\n\n{}".format(
                        self.current_room.guardian.drop))
                    self.player.inventory.append(
                        self.current_room.guardian.drop)
                    self.current_room.guardian = None

            elif main_choice == 'treasure':
                if self.current_room.guardian is not None:
                    spaced_print("You must defeat the guardian first.",
                                 pre=False)
                    continue
                spaced_print("Treasure:\n{}".format(
                    str(self.current_room.treasure)))
                treasure_choice = prompt(['take', 'back'])

                if treasure_choice == 'back':
                    continue
                elif treasure_choice == 'take':
                    spaced_print(self.current_room.treasure.full_info())
                    print "You acquired {}".format(
                        self.current_room.treasure.name)
                    self.player.inventory.append(self.current_room.treasure)
                    self.current_room.treasure = None

    def end_game_defeat(self, defeat_exception):
        "Takes a defeat exception and ends the game."
        import sys

        if isinstance(defeat_exception, PlayerDeadException):
            print "\nIf at first you don't succeed; call it version 1.0."
            sleep(1)
            print "    -- Unknown"

            sleep(1)
            print "\nYou've fought valiantly, but have been killed."
            sleep(1)
        else:
            sleep(1)
            print str(defeat_exception)
        sys.exit(0)

    def end_game_victory(self, victory_exception):
        "Takes a victory exception and ends the game."
        import sys

        if isinstance(victory_exception, FinalBossDeadException):
            print "\nImpossible is just a big word thrown around by small men"
            sleep(0.5)
            print "who find it easier to live in the world they've been given"
            sleep(0.5)
            print "than to explore the power they have to change it."
            sleep(0.5)
            print "Impossible is not a fact - it's an opinion. Impossible is"
            sleep(0.5)
            print "not a declaration - it's a dare. Impossible is potential."
            sleep(0.5)
            print "Impossible is temporary. Impossible is nothing."
            sleep(0.5)
            print "    -- Muhammad Ali"
            sleep(1)

            print "\nYou've destroyed the King of Shadow and vanquished the"
            print "shadows from the Brain. You have changed the world."
            print "Well done."
        sys.exit(0)


def fight(player, monster, monster_name='monster', can_run=True):
    "Fights a monster and a player with user input."
    print "You are fighting {}".format(monster.name)

    while True:
        try:
            spaced_print("{}:\n{}".format(monster_name.capitalize(),
                                          monster.format_stats()))
            spaced_print("You:\n{}".format(player.format_stats()),
                         pre=False)

            if can_run:
                fight_choice = prompt(['attack', 'run'])
            else:
                print "You can't run."
                fight_choice = prompt(['attack'])

            if fight_choice == 'attack':
                player_multiplier = random() + 0.5
                player_damage = int(player.attack * player_multiplier)

                monster_multiplier = random() + 0.5
                monster_damage = int(monster.attack * monster_multiplier)

                order = random()
                if order <= 0.5:
                    spaced_print("You did {} damage!".format(player_damage))
                    monster.health -= player_damage

                    spaced_print("The {} did {} damage!".format(
                        monster_name, monster_damage), pre=False)
                    player.health -= monster_damage
                else:
                    spaced_print("The {} did {} damage!".format(
                        monster_name, monster_damage))
                    player.health -= monster_damage

                    spaced_print("You did {} damage!".format(player_damage),
                                 pre=False)
                    monster.health -= player_damage

            elif fight_choice == 'run':
                raise AbortFightException()

        except MonsterDeadException:
            spaced_print("You killed the {}!".format(monster_name), pre=False)
            raise


def prompt(options):
    "Prompts for a choice from the given options."
    while True:
        choice = raw_input("What would you like to do?\n({}): ".format(
            "/".join(options)))
        if choice in options:
            return choice
        print "{} is not a valid option. Please choose again.".format(
            choice)
