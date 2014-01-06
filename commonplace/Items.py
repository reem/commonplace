"""
Jonathan Reem
Implements the base classes for items such as equipment.
"""

__all__ = ['BaseItem', 'BaseEquipment']

from commonplace.Base import BaseObj


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

    def __str__(self):
        return BaseItem.__str__(self) + '\n' + self._stat_format()

    def __repr__(self):
        return BaseItem.__repr__(self) + '\n' + self._stat_format()

class BaseTreasure(BaseItem):
    def __init__(self, name, description):
        BaseItem.__init__(self, name, description, 'Treasure')

class PoemTreasure(BaseTreasure):
    def __init__(self, name, description, category):
        BaseTreasure.__init__(self, name, description)
        self.category = category
