"""
Jonathan Reem
January 2014

Generates all game objects.
"""

import commonplace.Items as Items
import commonplace.Monster as Monster
from commonplace.Quotes import QUOTES
from commonplace.ItemList import ITEMS
# pylint: disable=R0903, R0913


def generate_all():
    "Generates a player and map."
    return (generate_player(), generate_map())


def generate_player():
    "Generates a player."
    pass


def generate_map():
    "Generates a map."
    pass

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


def generate_monster(monster_template):
    "Generates a monster from a monster_template"
    quote = QUOTES[monster_template.category].pop()
    drop = generate_item(monster_template.category,
                         monster_template.strength)

    return monster_template.correct_constructor(monster_template.name,
                                                monster_template.description,
                                                drop, str(quote))


class MonsterTemplate(object):
    "Template to generate a monster."
    _strength_to_constructor = {
        1: Monster.BrainMonster.shadow_knight,
        2: Monster.BrainMonster.shadow_giant,
        3: Monster.BrainMonster.shadow_gargantuan,
        4: Monster.BrainMonster.shadow_guardian
    }

    def __init__(self, name, description, category, strength):
        self.name = name  # String
        self.description = description  # String
        self.category = category  # String
        self.strength = strength  # Int from 1 -> 4

    def correct_constructor(self):
        "Returns the appropriate BrainMonster constructor to use."
        return self._strength_to_constructor[self.strength]


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
        'weapon', {'health': -500, 'attack': 2000},
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
        'armor', {'health': 1000, 'attack': -200},
        "In the midst of Winter ...\n    - Albert Camus"),

    Items.BrainEquipment(
        "Ring of Winter",
        "The ring is frighteningly cold and exudes an aura of protection.",
        'armor', {'health': 500, 'attack': -100},
        "In the midst of Winter ...\n    - Albert Camus"))
