"""
Jonathan Reem
January 2014

Generates all game objects.
"""

import commonplace.Items as Items
import commonplace.Monster as Monster
import commonplace.Player as Player
import commonplace.Rooms as Rooms
import commonplace.Places as Places

from commonplace.Quotes import QUOTES
from commonplace.ItemList import ITEMS
from commonplace.Map import MAP
from commonplace.MonsterList import MONSTERS
# pylint: disable=R0903, R0913


def generate_all():
    "Generates a player and map."
    return (generate_player(), generate_map())


def generate_player():
    "Generates a player."
    return Player.BrainPlayer("Commonplace Warrior",
                              "A warrior sent by the commonplace coalition ",
                              "to destroy the shadows that have invaded "
                              "the Brain.",
                              [], 100, 20)

def generate_hall(hall_template):
    "Generates a hall."
    pass

def generate_throne(throne_template):
    "Generates a throne."
    pass

def generate_room(room_template):
    """
    Generates a room from a template.
    NOTE: You need to run fix_doors on the list of rooms after
    generating them or the doors will not work properly.
    """
    difficulty_lookup = {
        1: 1,
        2: 2,
        3: 4,
        4: 8
    }

    if room_template.name == "Hall":
        return generate_hall(room_template)
    elif room_template.name == "Throne":
        return generate_throne(room_template)

    Monster.BrainMonster.set_difficulty(
        difficulty_lookup[room_template.difficulty])
    monster = generate_monster(next(MONSTERS),
                               room_template.category)

    if room_template.quote is None:
        quote = QUOTES[room_template.category].pop()
    else:
        quote = room_template.quote

    return Rooms.BrainRoom(room_template.name,
                           room_template.description,
                           room_template.doors,
                           str(quote),
                           generate_item(room_template.category,
                                         room_template.difficulty),
                           [], [monster])

def fix_doors(rooms):
    "Changes index based doors to real references."
    for room in rooms:
        for direction in room.doors:
            room.doors[direction] = rooms[room.doors[direction]]
    return rooms

def generate_map():
    "Generates the map."
    map_template = MAP
    rooms = [generate_room(room_template)
             for room_template in map_template.rooms]
    rooms = fix_doors(rooms)

    return Places.BaseMap(map_template.name,
                          map_template.description,
                          rooms, 0)

def generate_item(category, strength):
    "Generates an item appropriate for a category and strength."
    item_template = ITEMS[category][strength].pop()
    quote = QUOTES[category].pop()
    health, attack = stats_from_template(item_template)
    stats = {'health': health, 'attack': attack}
    return Items.BrainEquipment(item_template.name, item_template.description,
                                item_template.item_type.lower(),
                                quote, stats)

def stats_from_template(item_template):
    "Gets the correct stats for equipment."
    helmet_lookup = {
        1: (20, 0),
        2: (50, 0),
        3: (100, 20),
        4: (200, 40)
    }

    armor_lookup = {
        1: (50, 0),
        2: (150, 0),
        3: (450, 0),
        4: (1400, 0)
    }

    shield_lookup = {
        1: (30, 15),
        2: (60, 30),
        3: (100, 50),
        4: (200, 120)
    }

    sword_lookup = {
        1: (0, 20),
        2: (0, 100),
        3: (0, 500),
        4: (0, 2500)
    }

    ring_lookup = {
        1: (20, 20),
        2: (45, 60),
        3: (100, 150),
        4: (200, 300)
    }

    master_lookup = {
        'helmet': helmet_lookup,
        'armor': armor_lookup,
        'shield': shield_lookup,
        'sword': sword_lookup,
        'ring': ring_lookup
    }

    return master_lookup[item_template.item_type][item_template.strength]


def generate_monster(monster_template, category):
    "Generates a monster from a monster_template"
    quote = QUOTES[monster_template.category].pop()
    drop = generate_item(category,
                         monster_template.strength)

    return monster_template.correct_constructor(monster_template.name,
                                                monster_template.description,
                                                drop, str(quote))


class ItemSet(object):
    "Groups a set of items."
    def __init__(self, name, sword, helmet, shield, armor, ring):
        self.name = name
        self.sword = sword
        self.helmet = helmet
        self.shield = shield
        self.armor = armor
        self.ring = ring
        self.items = [sword, helmet, shield, armor, ring]

SUMMER_WINTER_SET = ItemSet(
    "Summer/Winter Set",
    Items.BrainEquipment(
        "Sword of Invincible Summer", "The sword glows a fiery red.",
        'weapon', {'health': -1000, 'attack': 5000},
        "... I found there was, within me, an invincible summer."
        "\n    - Albert Camus"),

    Items.BrainEquipment(
        "Helmet of Winter", "The helmet is cold and heavy, but unblemished.",
        'helmet', {'health': 250, 'attack': -50},
        "In the midst of Winter ...\n    - Albert Camus"),

    Items.BrainEquipment(
        "Shield of Winter", "The shield is cold and heavy, but unblemished.",
        'shield', {'health': 500, 'attack': -100},
        "In the midst of Winter ...\n    - Albert Camus"),

    Items.BrainEquipment(
        "Armor of Winter",
        "The armor is cold and extremely heavy, but unblemished.",
        'armor', {'health': 2000, 'attack': -200},
        "In the midst of Winter ...\n    - Albert Camus"),

    Items.BrainEquipment(
        "Ring of Winter",
        "The ring is frighteningly cold and exudes an aura of protection.",
        'armor', {'health': 500, 'attack': -100},
        "In the midst of Winter ...\n    - Albert Camus"))
