"""
Jonathan Reem

Implements BaseRoom and BaseMap classes
"""

__all__ = ['BaseRoom', 'BaseMap']

from commonplace.Base import BaseObj


class BaseRoom(BaseObj):
    """
    Your class should inherit this class, which has the basic mandatory
    info for the built-in game logic.
    """
    def __init__(self, name, description, doors):
        """
        doors: the rooms that this room links to, as a dictionary like:
            direction: room
              where direction is a direction such as "right" or "north"
              and room is the room that direction links to.

              NOTE: The burden is on YOU to provide consistent directions.
        """

        if type(doors) != dict:
            raise TypeError("doors should be a dictionary")

        BaseObj.__init__(self, name, description)
        self.doors = doors
        self.directions = set(self.doors.iterkeys())

    @property
    def valid_options(self):
        result = ["back"]
        if self.doors != {}:
            result.append('doors')


class BaseMap(BaseObj):
    """
    Your Map class should inherit this class, which has the mandatory
    attributes and methods for the built-in game logic.
    """
    def __init__(self, name, description, rooms, start_room=0):
        """
        rooms: a list of Rooms to add to the map
        start_room: optional index of the starting room in the rooms list
        """

        if not isinstance(start_room, int):
            raise TypeError("start_room should be an integer index of rooms.")
        if not 0 <= start_room < len(rooms):
            raise ValueError("start_room should be a valid index of rooms.")

        BaseObj.__init__(self, name, description)
        self.rooms = rooms
        self.start_room = rooms[start_room]
