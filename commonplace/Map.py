"""
Jonathan Reem
January 2014

Holds the Map Template
"""

from operator import contains

# pylint: disable=R0903, R0913
from commonplace.Quotes import CATEGORIES
from commonplace.Base import assert_with_dump
from commonplace.Rooms import PoemRoom

NORTH = 'N'
NORTHEAST = 'NE'
SOUTHEAST = 'SE'
SOUTH = 'S'
SOUTHWEST = 'SW'
NORTHWEST = 'NW'

DIRECTIONS = set(NORTH, NORTHEAST, SOUTHEAST,
                 SOUTH, SOUTHWEST, NORTHWEST)


class MapTemplate(object):
    "Template for generating a map."
    def __init__(self, name, description, rooms, start_room):
        self.name = name                # String
        self.description = description  # String

        for room in rooms:
            assert_with_dump(room, lambda d: type(d) == RoomTemplate)
        self.rooms = rooms              # [RoomTemplate]

        assert_with_dump(range(len(rooms)), start_room, contains)
        self.start_room = start_room    # Index of rooms


class RoomTemplate(object):
    "Template for generating a room."
    def __init__(self, name, description, doors, difficulty, category):
        self.name = name                # String
        self.description = description  # String

        assert_with_dump(doors, lambda d: type(d) == dict)
        for direction in doors:
            assert_with_dump(DIRECTIONS, direction, contains)
            assert_with_dump(range(27), doors[direction], contains)

        self.doors = doors              # {direction: RoomTemplate INDEX}

        assert_with_dump(range(1, 5), difficulty, contains)
        self.difficulty = difficulty    # Int (1->4)

        assert_with_dump(CATEGORIES, category, contains)
        self.category = category        # String

# TODO: IMPLEMENT REAL CATEGORIES.
cat1 = 'test_category'
cat2 = 'test_category'
cat3 = 'test_category'
cat4 = 'test_category'
cat5 = 'test_category'

CATEGORIES = 'test_category'

MAP = MapTemplate(
    "The Brain",
    "Usually a place of rapid activity, the Brain is currently under attack by"
    " the shadows. Destroy the shadow king and collect the wisps of thought "
    "that the shadows are guarding.",
    [
        RoomTemplate(
            "Entrance Segment",
            "It's dark and squishy everywhere. You've managed to enter but"
            " don't know where you are.",
            {NORTH: 1},
            1, cat1
        ),
        RoomTemplate(
            "A Junction",
            "There is a fork in the path. Continue onward or divert, the "
            "choice is yours.",
            {NORTH: 5,
             SOUTHWEST: 2,
             SOUTH: 0},
            1, cat1
        ),
        RoomTemplate(
            "The Left Choice",
            "The tunnel appears to go onward. There are shadows eveywhere.",
            {NORTHWEST: 3,
             NORTHEAST: 1},
            1, cat2
        ),
        RoomTemplate(
            "Hall",
            "",
            {NORTH: 4,
             SOUTHEAST: 2},
            2, cat2
        ),
        RoomTemplate(
            "Throne",
            "",
            {SOUTH, 3},
            3, cat2
        ),
        RoomTemplate(
            "Onward",
            "The path is blocked ahead. You must turn to continue.",
            {SOUTHWEST: 6,
             SOUTH: 1},
            1, cat1
        ),
        RoomTemplate(
            "Language Segment",
            "It's bright in this segment as strange letters dance around"
            " in the air. Statements and expressions make their home here.",
            {NORTHEAST: 5,
             NORTH: 7},
            2, cat1
        ),
        RoomTemplate(
            "The Great Schism",
            "There is a great crossroads here. It appears as if this "
            "segment is usually bustling with activity as messages "
            "travel from one end of the Brain to another. Which road "
            "will you take?",
            {NORTHEAST: 14,
             NORTH: 8,
             SOUTH: 6},
            2, cat1
        ),
        RoomTemplate(
            "A Transform",
            "This segment is split between two different areas. One "
            "appears similar to the segments you have visited, the other "
            "CATEGORY 3.",  # TODO
            {SOUTH: 7,
             SOUTHWEST: 9},
            2, cat3
        ),
        RoomTemplate(
            "New Territory",
            "The shadows are getting much larger here. Everything is "
            "darker and you hear noises everywhere.",
            {NORTHEAST: 8,
             NORTH: 10},
            3, cat3
        ),
        RoomTemplate(
            "Hall",
            "",
            {NORTH: 11,
             NORTHEAST: 12,
             SOUTH: 9},
            3, cat3
        ),
        RoomTemplate(
            "Throne",
            "",
            {SOUTH: 10},
            4, cat3
        ),
        RoomTemplate(
            "The Guards",
            "It seems you are nearing the king of shadows. This segment hosts "
            "his guards, you will have to kill them before you can move on.",
            {SOUTHWEST: 10,
             NORTHEAST: 13},
            4, cat1
        ),
        RoomTemplate(
            "Hall",
            "",
            {NORTH: 26,
             SOUTHWEST: 12},
            4, cat1
        ),
        RoomTemplate(
            "Mystery",
            "You've ventured off the path, into another area full of shadows "
            "and darkness. It is hard to see anything.",
            {NORTH: 15,
             SOUTHWEST: 7},
            2, cat4
        ),
        RoomTemplate(
            "Channel",
            "There is a long straight path here. Shadows are behind every "
            "corner.",
            {NORTHWEST: 15,
             SOUTHEAST: 17},
            3, cat4
        ),
        RoomTemplate(
            "Split",
            "The channel ends in a split, you can go north or south. "
            "Each direction looks starkly different.",
            {SOUTH: 21,
             NORTH: 18},
            3, cat4
        ),
        RoomTemplate(
            "North",
            "This territory is similar to the channel. It is "
            "CATEGORY 4",  # TODO
            {NORTHWEST: 19,
             SOUTH: 17},
            4, cat4
        ),
        RoomTemplate(
            "Hall",
            "",
            {NORTHEAST: 20,
             SOUTHEAST: 18},
            4, cat4
        ),
        RoomTemplate(
            "Throne",
            "",
            {SOUTHWEST: 19},
            4, cat4
        ),
        RoomTemplate(
            "South",
            "This territory is starkly different. CATEGORY 5",  # TODO
            {NORTH: 17,
             NORTHWEST: 22},
            3, cat5
        ),
        RoomTemplate(
            "A Corner",
            "Most ways out are blocked in this dark area. You must "
            "continue or risk getting stuck.",
            {SOUTH: 23,
             SOUTHEAST: 21},
            3, cat5
        ),
        RoomTemplate(
            "CATEGORY 5 NAME",  # TODO
            "",  # TODO
            {SOUTHEAST: 24,
             NORTH: 22},
            4, cat5
        ),
        RoomTemplate(
            "Hall",
            "",
            {SOUTHWEST: 25,
             NORTHWEST: 23},
            4, cat5
        ),
        RoomTemplate(
            "Throne",
            "",
            {},
            5, cat1
        ),
    ],
    0)

THRONE_ROOMS = {
    cat1: PoemRoom(
    ),
    cat2: PoemRoom(
    ),
    cat3: PoemRoom(
    ),
    cat4: PoemRoom(
    ),
    cat5: PoemRoom(
    )
}
