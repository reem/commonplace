"""
Jonathan Reem
January 2014

Generates all game objects.
"""

import commonplace.Items as Items
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


def generate_monster(monster_template):
    "Generates a monster from a monster_template"
    pass


class MonsterTemplate(object):
    "Template to generate a monster."
    def __init__(self, name, description, category, strength):
        self.name = name
        self.description = description
        self.category = category
        self.strength = strength


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
