"""
Jonathan Reem
Implements the base classes for items such as equipment.
"""

__all__ = ['BaseItem', 'BaseEquipment']

from commonplace.Base import BaseObj, format_objects


class BaseItem(BaseObj):
    """
    Items should inherit from this class, and should define their item_type
    in their constructor. See BaseEquipment for an example.
    """
    def __init__(self, name, description, item_type):
        BaseObj.__init__(self, name, description)
        self.item_type = item_type


class BaseEquipment(BaseItem):
    """
    Equipment should inherit from this class.

    eq_type: type of equipment, such as armor or sword
    stats: a dictionary of {stat: boost} pairs.
        "boost" can be negative!
    """
    def __init__(self, name, description, eq_type, stats):
        BaseItem.__init__(self, name, description, 'Equipment')
        self.eq_type = eq_type
        self.stats = stats

    def format_stats(self):
        "Formats stats for pretty-printing"
        return "Stats:\n" + format_objects(self.stats)

    def full_info(self):
        return str(self)

    def __str__(self):
        return BaseItem.__str__(self) + '\n' + self.format_stats()

    def __repr__(self):
        return BaseItem.__repr__(self) + '\n' + self.formatt_stats()


class BrainEquipment(BaseEquipment):
    def __init__(self, name, description, eq_type, stats, quote):
        BaseEquipment.__init__(self, name, description, eq_type, stats)
        self.quote = quote

    def __str__(self):
        return "{}\n{}\n{}".format(BaseItem.__str__(self), self.quote,
                                   self.format_stats())


class BaseTreasure(BaseItem):
    def __init__(self, name, description):
        BaseItem.__init__(self, name, description, 'Treasure')

    def fulL_info(self):
        return str(self)

    def __str__(self):
        return BaseItem.__str__(self) + '\n' + self.item_type


class PoemTreasure(BaseTreasure):
    def __init__(self, name, description, quote, category):
        BaseTreasure.__init__(self, name, description)
        self.category = category
        self.quote = quote

    def full_info(self):
        return "{}\n{}\n{}".format(BaseTreasure.__str__(self), self.quote
                                   self.category)
