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
    def __init__(self, name, description, start_inventory=None,
                 start_equipment=None, equipment_slots=DEF_EQUIP_SLOTS,
                 start_health=100):
        BaseObj.__init__(self, name, description)
        self._health = start_health
        self._base_health = start_health
        self.inventory = [] if start_inventory is None else start_inventory
        self.equipment = {} if start_equipment is None else start_equipment
        self.equipped = equipment_slots

    def attribute_bonus(self, attribute):
        return sum([equipment.stats[attribute] for _, equipment in self.equipped])

    @property
    def health(self):
        return self._health

    @property
    def max_health(self):
        return self._base_health + self.attribute_bonus('health')

    @health.setter
    def health(self, value):
        if value <= 0:
            raise PlayerDeadException
        elif self.health + value >= self.max_health:
            self._health = self.max_health
        else:
            self._health += value

    def equip(self, equipment, slot):
        if equipment not in self.equipment.iterkeys():
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
        result = "{0}:\n{1}".format(attribute.capitalize(),
                                    format_objects(getattr(self, attribute)))


class BrainPlayer(BasePlayer):
    def __init__(self, name, description, start_inventory,
                 start_equipment, equipment_slots=DEF_EQUIP_SLOTS,
                 start_health, base_attack):
        BasePlayer.__init__(self, name, description, start_inventory,
                            start_equipment, equipment_slots, start_health)
        self._attack = base_attack

    @property
    def attack(self):
        return self._attack + self.attribute_bonus('attack')

    def full_info(self):
        return "{0}\n{1}\n{}".format(self.format_stats(),
                                     format_objects(self.equipment),
                                     format_objects(self.equipped))

    def format_stats(self):
        return "Health: {0}/{1}\nAttack: {2}+{3}".format(self.health,
                                                         self.max_health,
                                                         self._attack,
                                                         self.attribute_bonus(
                                                             'attack'))
