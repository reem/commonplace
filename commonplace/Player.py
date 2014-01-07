"""
Jonathan Reem
January 2013

Implements the Player class.
"""


from commonplace.Base import BaseObj, format_objects
from commonplace.Exceptions import PlayerDeadException

DEF_EQUIP_SLOTS = {'helmet': None,
                   'armor': None,
                   'weapon': None,
                   'shield': None,
                   'ring': None}


class BasePlayer(BaseObj):
    """Base Player class. All Player classes inherit from this."""
    def __init__(self, name, description, start_health,
                 base_attack, start_inventory=None,
                 equipment_slots=DEF_EQUIP_SLOTS):
        BaseObj.__init__(self, name, description)
        self._health = start_health
        self._base_health = start_health
        self._base_attack = base_attack
        self.inventory = [] if start_inventory is None else start_inventory
        self.equipped = equipment_slots

    def attribute_bonus(self, attribute):
        "Gets the bonus from equipment to a specific stat."
        return sum([equipment.stats[attribute]
                    for _, equipment in self.equipped])

    @property
    def health(self):
        "Gets current health."
        return self._health

    @property
    def max_health(self):
        "Gets the maximum possible health."
        return self._base_health + self.attribute_bonus('health')

    @health.setter
    def health(self, value):
        "Sets health, checks for death and overflow."
        if value <= 0:
            raise PlayerDeadException(None)
        elif value >= self.max_health:
            self._health = self.max_health
        else:
            self._health = value

    @property
    def attack(self):
        "Returns the current attack stat."
        return self._base_attack + self.attribute_bonus('attack')

    def equip(self, equipment, slot):
        "Equips an equipment."
        if equipment not in self.inventory:
            print "Attempted Equipment: {}".format(equipment.name)
            raise ValueError("Tried to equip equipment you don't have.")

        if slot not in self.equipped.iterkeys():
            print "Tried to equip to: {}".format(slot)
            raise ValueError("Tried to equip to a slot that is not valid.")

        if equipment.eq_type != slot:
            print "Tried to equip {} of eq_type {} to slot {}".format(
                equipment.name, equipment.eq_type, slot)
            raise ValueError("Tried to equip to the wrong kind of slot.")

        self.equipped[slot] = equipment

    def pretty_format(self, attribute):
        "Pretty format for an attribute."
        return "{0}:\n{1}".format(attribute.capitalize(),
                                  format_objects(getattr(self, attribute)))


class BrainPlayer(BasePlayer):
    "The player used in the Brain/Commonplace game."
    def __init__(self, name, description, start_inventory,
                 start_health, base_attack, equipment_slots=DEF_EQUIP_SLOTS):
        BasePlayer.__init__(self, name, description, start_health,
                            base_attack, start_inventory,
                            equipment_slots)

    def full_info(self):
        "Format everything."
        return "{}, {}\n{}\n{}\n{}".format(self.name, self.description,
                                               self.format_stats(),
                                               format_objects(self.inventory),
                                               format_objects(self.equipped))

    def format_stats(self):
        "Formatting stats for information purposes."
        return "Health: {0}/{1}\nAttack: {2}+{3}".format(self.health,
                                                         self.max_health,
                                                         self._base_attack,
                                                         self.attribute_bonus(
                                                             'attack'))
