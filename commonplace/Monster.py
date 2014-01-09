"""
Jonathan Reem
January 2014

Implements the BaseMonster, BrainMonster and PoemGuardian classes.
"""

from commonplace.Base import BaseObj
from commonplace.Exceptions import MonsterDeadException
# pylint: disable=R0913


class BaseMonster(BaseObj):
    "All monsters inherit from this monster. mwahaha."

    def __init__(self, name, description, start_health, attack, drop):
        BaseObj.__init__(self, name, description)
        self._health = start_health
        self.max_health = start_health
        self.attack = attack
        self.drop = drop

    @property
    def health(self):
        "Gets the current health of the monster."
        return self._health

    @health.setter
    def health(self, value):
        "Changes the health of the monster. Checks for death."
        if value <= 0:
            raise MonsterDeadException(str(self))
        else:
            self._health = value

    def maximize_health(self):
        "Sets the monsters health to maximum in case of run."
        self.health = self.max_health

    def full_info(self):
        "Full information for prompting."
        return "{}\nHealth: {}\nAttack: {}".format(BaseObj.__str__(self),
                                                   self.health,
                                                   self.attack)

    def format_stats(self):
        "Just stat information for fighting."
        return "Health: {}/{}\nAttack: {}".format(self.health,
                                                  self.max_health,
                                                  self.attack)


class BrainMonster(BaseMonster):
    "Implements monsters with quotes and multiple custom constructors.."
    _general_difficulty = 0.75
    __difficulty = 1

    def __init__(self, name, description, start_health, attack, drop,
                 quote, monster_type):
        start_health *= BrainMonster.__difficulty
        start_health *= BrainMonster._general_difficulty
        attack *= BrainMonster.__difficulty
        attack *= BrainMonster._general_difficulty
        start_health = int(start_health)
        attack = int(attack)

        BaseMonster.__init__(self, name, description, start_health,
                             attack, drop)
        self.quote = quote
        self.monster_type = monster_type

    @classmethod
    def shadow_knight(cls, name, description, drop, quote,
                      start_health=30, attack=6,
                      monster_type='knight'):
        "Alternative constructor with useful defaults."
        return cls(name, description, start_health, attack,
                   drop, quote, monster_type)

    @classmethod
    def shadow_gargantuan(cls, name, description, drop, quote,
                          start_health=100, attack=15,
                          monster_type='gargantuan'):
        "Alternative constructor with useful defaults."
        return cls(name, description, start_health, attack,
                   drop, quote, monster_type)

    @classmethod
    def shadow_giant(cls, name, description, drop, quote,
                     start_health=50, attack=10,
                     monster_type='giant'):
        "Alternative constructor with useful defaults."
        return cls(name, description, start_health, attack,
                   drop, quote, monster_type)

    @classmethod
    def shadow_guardian(cls, name, description, drop, quote,
                        start_health=200, attack=30,
                        monster_type='guardian'):
        "Alternative constructor for guardians."
        return cls(name, description, start_health, attack,
                   drop, quote, monster_type)

    @classmethod
    def set_difficulty(cls, value, increment=False):
        "Changes the __difficulty attribute for mass generation."
        if increment:
            cls.__difficulty += value
        else:
            cls.__difficulty = value

    def full_info(self):
        "Full information for prompting."
        return "{}\n{}\nHealth: {}\nAttack: {}".format(BaseObj.__str__(self),
                                                       self.quote,
                                                       self.health,
                                                       self.attack)
