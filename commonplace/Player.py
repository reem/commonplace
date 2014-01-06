"""
Jonathan Reem
January 2013

Implements the Player class.
"""


from commonplace.Base import BaseObj, format_objects

DEF_EQUIP_SLOTS = {'helmet': None,
                   'armor': None,
                   'weapon': None,
                   'shield': None,
                   'ring': None}


class BasePlayer(BaseObj):
    def __init__(self, name, description, start_attributes,
                 start_inventory=None, start_equipment=None,
                 equipment_slots=DEF_EQUIP_SLOTS):
        BaseObj.__init__(self, name, description)
        self.attributes = start_attributes
        self.inventory = [] if start_inventory is None else start_inventory
        self.equipment = {} if start_equipment is None else start_equipment
        self.equipped = equipment_slots

    def equip(self, equipment, slot):
        if equipment not in self.equipment.iterkeys():
            raise ValueError("Tried to equip equipment you don't have.")

        if slot not in self.equipped.iterkeys():
            raise ValueError("Tried to equip to a slot that is not valid.")

        self.equipped[slot] = equipment

    def pretty_format(self, attribute):
        result = "{0}:\n{1}".format(attribute.capitalize(),
                                    format_objects(getattr(self, attribute)))

