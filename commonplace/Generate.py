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

from random import randint
from commonplace.Quotes import QUOTES
from commonplace.ItemList import ITEMS
from commonplace.Map import (MAP, THRONE_ROOMS, SUMMER_WINTER_SET,
                             CAT1, CAT2, CAT3, CAT4, CAT5)
# pylint: disable=R0903, R0913, C0301

QUOTES_GENERATED = {
    CAT1: 1,
    CAT2: 1,
    CAT3: 1,
    CAT4: 1,
    CAT5: 1
}

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

def generate_throne(throne_template):
    "Generates a throne."
    throne_room = THRONE_ROOMS[throne_template.category]
    throne_room.doors = throne_template.doors
    return throne_room

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

    if room_template.name == "Throne":
        return generate_throne(room_template)

    if not room_template.has_monster:
        monster = []
    else:
        Monster.BrainMonster.set_difficulty(
            difficulty_lookup[room_template.difficulty])
        monster = generate_monster(randint(1, 3),
                                   room_template.category,
                                   room_template.difficulty)

    if room_template.quote is None:
        try:
            quote = QUOTES[room_template.category].pop()
            QUOTES_GENERATED[room_template.category] += 1
        except IndexError:
            print room_template.category
            print QUOTES_GENERATED[room_template.category]
            raise
    else:
        quote = room_template.quote

    return Rooms.BrainRoom(room_template.name,
                           room_template.description,
                           room_template.doors,
                           str(quote),
                           [], [], [monster])

def fix_doors(rooms):
    "Changes index based doors to real references."
    for room in rooms:
        for direction in room.doors:
            try:
                room.doors[direction] = rooms[room.doors[direction]]
            except IndexError:
                print room.doors[direction]
                raise
    return rooms

def generate_map():
    "Generates the map."
    map_template = MAP
    rooms = [generate_room(room_template)
             for room_template in map_template.rooms]
    rooms = fix_doors(rooms)

    return Places.BaseMap(map_template.name,
                          map_template.description,
                          rooms, map_template.start_room)

def generate_item(category, strength):
    "Generates an item appropriate for a category and strength."
    try:
        item_template = ITEMS[category][strength].pop()
    except IndexError:
        print category, strength
        raise

    if item_template.name == "Sword of Invincible Summer":
        return SUMMER_WINTER_SET.sword

    try:
        quote = QUOTES[category].pop()
        QUOTES_GENERATED[category] += 1
    except IndexError:
        print category
        print QUOTES_GENERATED[category]
        raise

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

MONSTER_LOOKUP = {
    1: ("Shadow Knight",
        "A human sized, sword wielding shadow. These are the most commonplace."),
    2: ("Shadow Giant",
        "Standing at about twice the size of people, a shadow giant is a threat "
        "to everything around it. Because of its general stupidity, that often "
        "includes itself."),
    3: ("Shadow Gargantuan",
        "These monstrosities crawl around on four arms and are large enough to "
        "swallow people in a single bite. Be wary of them.")
}

def generate_monster(strength, category, item_strength):
    "Generates a monster"

    strength_to_constructor = {
        1: Monster.BrainMonster.shadow_knight,
        2: Monster.BrainMonster.shadow_giant,
        3: Monster.BrainMonster.shadow_gargantuan,
    }

    try:
        quote = QUOTES[category].pop()
        QUOTES_GENERATED[category] += 1
    except IndexError:
        print category
        print QUOTES_GENERATED[category]
        raise

    drop = generate_item(category, item_strength)

    name, description = MONSTER_LOOKUP[strength]

    return strength_to_constructor[strength](name, description,
                                             drop, str(quote))
