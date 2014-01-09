"""
Jonathan Reem
January 2014

Exports a dictionary of Monsters formatted like:
    {category: [MonsterTemplate]}
"""

import commonplace.Monster as Monster
# pylint: disable=R0903


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
