"""
Author: Jonathan Reem
Implements room classes specifically for the Brain game.
Room classes inherit from Places.BaseRoom
"""

import commonplace.Places as pl
import commonplace.Base as base
# pylint: disable=R0913


class BrainRoom(pl.BaseRoom):
    "Class used for rooms in the game."
    def __init__(self, name, description, doors, quote, items, npcs, monsters):
        pl.BaseRoom.__init__(name, description, doors)
        self.quote = quote
        self.items = items
        self.npcs = npcs
        self.monsters = monsters

    def entrance_info(self):
        "Gives the info to display on entrance to the room."
        return "{0.name}\n{1}\n\n{0.quote}\n\n{0.description}".format(
            self, "-" * len(self.name))

    def full_info(self):
        "Gives the full information about the room."
        result = self.entrance_info()
        if self.doors != {}:
            result += "\n\nDoors:\n{0}".format(base.format_objects(self.doors))
        if self.items != []:
            result += "\n\nItems:\n{0}".format(base.format_objects(self.items))
        if self.npcs != []:
            result += "\n\nCharacters:\n{0}".format(
                base.format_objects(self.npcs))
        if self.monsters != []:
            result += "\n\nMonsters:\n{0}".format(
                base.format_objects(self.monsters))
        return result


class PoemRoom(pl.BaseRoom):
    "Class used for end rooms."
    def __init__(self, name, description, doors, poem, treasure, guardian):
        pl.BaseRoom.__init__(name, description, doors)
        self.poem = poem
        self.treasure = treasure
        self.guardian = guardian

    def entrance_info(self):
        "Gives the info to display on entrance to the room."
        return "{0.name}\n{1}\n\n{0.description}\n\n{0.poem}".format(
            self, "-" * len(self.name))

    def full_info(self, poem=True):
        """
        Gives the full information about the room, for PoemRooms this
        is mostly for debugging.
        """

        result = self.entrance_info()
        if self.poem != '' and poem:
            result += "\n\nPoem:\n{0.poem}".format(self)
        if self.treasure is not None:
            result += "\n\nTreasure:\n{0}".format(
                base.format_objects(self.treasure))
        if self.guardian is not None:
            result += "\n\nGuardian:\n{0}".format(
                base.format_objects(self.guardian))
        return result
