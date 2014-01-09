"""
Jonathan Reem
January 2014

Holds the Map Template
"""

from operator import contains

# pylint: disable=R0903, R0913, C0301
from commonplace.Quotes import CATEGORIES, QUOTES, Quote
from commonplace.Base import assert_with_dump
from commonplace.Rooms import PoemRoom
from commonplace.Poems import POEMS
from commonplace.Items import BrainEquipment
from commonplace.Monster import BrainMonster

NORTH = 'N'
NORTHEAST = 'NE'
SOUTHEAST = 'SE'
SOUTH = 'S'
SOUTHWEST = 'SW'
NORTHWEST = 'NW'

DIRECTIONS = set([NORTH, NORTHEAST, SOUTHEAST,
                  SOUTH, SOUTHWEST, NORTHWEST])


class MapTemplate(object):
    "Template for generating a map."
    def __init__(self, name, description, rooms, start_room):
        self.name = name                # String
        self.description = description  # String

        for room in rooms:
            assert_with_dump(room, callback=lambda d: type(d) == RoomTemplate)
        self.rooms = rooms              # [RoomTemplate]

        assert_with_dump(range(len(rooms)), start_room,
                         callback=contains)
        self.start_room = start_room    # Index of rooms


class RoomTemplate(object):
    "Template for generating a room."
    def __init__(self, name, description, doors, difficulty, category,
                 quote=None, has_monster=True):
        self.name = name                # String
        self.description = description  # String

        assert_with_dump(doors, callback=lambda d: type(d) == dict)
        for direction in doors:
            assert_with_dump(DIRECTIONS, direction,
                             callback=contains)
            assert_with_dump(range(27), doors[direction],
                             callback=contains)

        self.doors = doors              # {direction: RoomTemplate INDEX}

        assert_with_dump(range(1, 6), difficulty,
                         callback=contains)
        self.difficulty = difficulty    # Int (1->4)

        assert_with_dump(CATEGORIES, category,
                         callback=contains)
        self.category = category        # String

        self.quote = quote
        self.has_monster = has_monster

CAT1 = 'CSSM'
CAT2 = 'IE'
CAT3 = 'SCW'
CAT4 = 'DPCW'
CAT5 = 'TPW'

assert set([CAT1, CAT2, CAT3, CAT4, CAT5]) == CATEGORIES

MAP = MapTemplate(
    "The Brain",
    "Usually a place of rapid activity, the Brain is currently under attack by"
    " the shadows. Destroy the shadow king and collect the wisps of thought "
    "that the shadows have taken.",
    [
        RoomTemplate(
            "The Entrance Segment",
            "It's dark and squishy everywhere. You've managed to enter but"
            " don't know where you are.",
            {NORTH: 1},
            1, CAT1,
            quote=Quote("To be nobody but yourself in a world which is "
                        "doing its best, night and day, to make you "
                        "everybody else means to fight the hardest "
                        "battle which any human being can fight; and never "
                        "stop fighting.", "e.e. cumming", CAT1),
            has_monster = False
        ),
        RoomTemplate(
            "A Junction",
            "There is a fork in the path. Continue onward or divert, the "
            "choice is yours.",
            {NORTH: 5,
             SOUTHWEST: 2,
             SOUTH: 0},
            1, CAT1
        ),
        RoomTemplate(
            "The Left Choice",
            "The tunnel appears to go onward. There are shadows eveywhere.",
            {NORTHWEST: 3,
             NORTHEAST: 1},
            1, CAT2
        ),
        RoomTemplate(
            "Hall of the Elite",
            "The walls are plated gold.",
            {NORTH: 4,
             SOUTHEAST: 2},
            2, CAT2
        ),
        RoomTemplate(
            "Throne",
            "",
            {SOUTH: 3},
            3, CAT2
        ),
        RoomTemplate(
            "Onward",
            "The path is blocked ahead. You must turn to continue.",
            {SOUTHWEST: 6,
             SOUTH: 1},
            1, CAT1
        ),
        RoomTemplate(
            "Language Segment",
            "It's bright in this segment as strange letters dance around"
            " in the air. Statements and expressions make their home here.",
            {NORTHEAST: 5,
             NORTH: 7},
            2, CAT1
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
            2, CAT1,
            quote=Quote("Whenever at a crossroads, do what the person"
                        " you want to be would do.", "Anonymous", CAT1),
            has_monster=False
        ),
        RoomTemplate(
            "A Transform",
            "This segment is split between two different areas. One "
            "appears similar to the segments you have visited, the other "
            "appears world changing.",
            {SOUTH: 7,
             SOUTHWEST: 9},
            3, CAT3
        ),
        RoomTemplate(
            "New Territory",
            "The shadows are getting much larger here. Everything is "
            "darker and you hear noises everywhere.",
            {NORTHEAST: 8,
             NORTH: 10},
            3, CAT3
        ),
        RoomTemplate(
            "Hall of Worlds",
            "This is clearly a transaction hub. The remains of great work "
            "still lay here.",
            {NORTH: 11,
             NORTHEAST: 12,
             SOUTH: 9},
            4, CAT3
        ),
        RoomTemplate(
            "Throne",
            "",
            {SOUTH: 10},
            4, CAT3
        ),
        RoomTemplate(
            "The Guards",
            "It seems you are nearing the king of shadows. This segment hosts "
            "his guards, you will have to kill them before you can move on.",
            {SOUTHWEST: 10,
             NORTHEAST: 13},
            4, CAT1
        ),
        RoomTemplate(
            "Hall of Mathematics",
            "The hall is empty, save the endless numbers scrawled on every "
            "surface.",
            {NORTH: 26,
             SOUTHWEST: 12},
            4, CAT1,
            has_monster = False
        ),
        RoomTemplate(
            "Mystery",
            "You've ventured off the path, into another area full of shadows "
            "and darkness. It is hard to see anything.",
            {NORTH: 15,
             SOUTHWEST: 7},
            2, CAT4
        ),
        RoomTemplate(
            "Channel",
            "There is a long straight path starting here. Shadows are everywhere.",
            {SOUTH: 14,
             SOUTHEAST: 16},
            2, CAT4
        ),
        RoomTemplate(
            "Channel",
            "The path continues.",
            {NORTHWEST: 15,
             SOUTHEAST: 17},
            3, CAT4
        ),
        RoomTemplate(
            "Split",
            "The channel ends in a split, you can go north or south. "
            "Each direction looks starkly different.",
            {SOUTH: 21,
             NORTH: 18,
             NORTHWEST: 16},
            3, CAT4,
            has_monster=False
        ),
        RoomTemplate(
            "North",
            "This territory is similar to the channel. It is "
            "full of darkness and pessimism.",
            {NORTHWEST: 19,
             SOUTH: 17},
            4, CAT4
        ),
        RoomTemplate(
            "Hall of Cynicism",
            "A plain wooden hall leading to a throne room.",
            {NORTHEAST: 20,
             SOUTHEAST: 18},
            4, CAT4
        ),
        RoomTemplate(
            "Throne",
            "",
            {SOUTHWEST: 19},
            4, CAT4
        ),
        RoomTemplate(
            "South",
            "This territory is starkly different. It is full of words, "
            "the shadows seem to fear their power and run from them.",
            {NORTH: 17,
             NORTHWEST: 22},
            3, CAT5
        ),
        RoomTemplate(
            "A Corner",
            "Most ways out are blocked in this dark area. You must "
            "continue or risk getting stuck.",
            {SOUTH: 23,
             SOUTHEAST: 21},
            3, CAT5
        ),
        RoomTemplate(
            "Library",
            "This room is full of books and knowledge.",
            {SOUTHEAST: 24,
             NORTH: 22},
            4, CAT5
        ),
        RoomTemplate(
            "Hall of Words",
            "This hall is covered in words. The floor is stitched "
            "from letters.",
            {SOUTHWEST: 25,
             NORTHWEST: 23},
            4, CAT5
        ),
        RoomTemplate(
            "Throne",
            "",
            {NORTHEAST: 24},
            4, CAT5
        ),
        RoomTemplate(
            "Throne",
            "",
            {},
            5, CAT1
        ),
    ],
    0)

class ItemSet(object):
    "Groups a set of items."
    def __init__(self, name, sword, helmet, shield, armor, ring):
        self.name = name
        self.sword = sword
        self.helmet = helmet
        self.shield = shield
        self.armor = armor
        self.ring = ring
        self.items = [sword, helmet, shield, armor, ring]

SUMMER_WINTER_SET = ItemSet(
    "Summer/Winter Set",
    BrainEquipment(
        "Sword of Invincible Summer", "The sword glows a fiery red.",
        'weapon', {'health': -1000, 'attack': 5000},
        "... I found there was, within me, an invincible summer."
        "\n    - Albert Camus"),

    BrainEquipment(
        "Helmet of Winter", "The helmet is cold and heavy, but unblemished.",
        'helmet', {'health': 400, 'attack': -50},
        "In the midst of Winter ...\n    - Albert Camus"),

    BrainEquipment(
        "Shield of Winter", "The shield is cold and heavy, but unblemished.",
        'shield', {'health': 500, 'attack':  100},
        "In the midst of Winter ...\n    - Albert Camus"),

    BrainEquipment(
        "Armor of Winter",
        "The armor is cold and extremely heavy, but unblemished.",
        'armor', {'health': 300, 'attack': -200},
        "In the midst of Winter ...\n    - Albert Camus"),

    BrainEquipment(
        "Ring of Winter",
        "The ring is frighteningly cold and exudes an aura of protection.",
        'armor', {'health': 600, 'attack': 200},
        "In the midst of Winter ...\n    - Albert Camus"))

THRONE_ROOMS = {
    CAT1: PoemRoom("Throne of Mathematics",
                   "Numbers, wires, and computers line the halls of this "
                   "room.",
                   {}, POEMS[0],
                   None,
                   BrainMonster("King of Shadows",
                                "He is dark and his features "
                                "are impossible to make out. He is standing "
                                "on a mound of dead challengers.",
                                20000, 600, None,
                                str(Quote("In the long run, understanding is always "
                                          "more important than getting things done. "
                                          "Why? Because if you get things done "
                                          "without understanding what you're doing,"
                                          " you're probably doing them wrong.",
                                          "Daniel Mclaury - http://qr.ae/Iga8l",
                                          CAT1)),
                                monster_type='FinalBoss')

    ),
    CAT2: PoemRoom("Throne of Snobbery",
                   "Books and words line the halls of this room.",
                   {}, POEMS[1],
                   None,
                   BrainMonster.shadow_guardian("Guardian of Words",
                                                "His armor is covered with obscure "
                                                "glyphs that nobody knows.",
                                                SUMMER_WINTER_SET.helmet,
                                                str(QUOTES[CAT2].pop()))
    ),
    CAT3: PoemRoom("Throne of the World",
                   "This room has the vestiges of a busy place. World changing work "
                   "is done here.",
                   {}, POEMS[2],
                   None,
                   BrainMonster.shadow_guardian("Guardian of Work",
                                                "He shifts restlessly, awaiting your "
                                                "challenge.",
                                                SUMMER_WINTER_SET.armor,
                                                str(QUOTES[CAT3].pop()))
    ),
    CAT4: PoemRoom("Throne of Cynicism",
                   "A plain room with a large wooden throne.",
                   {}, POEMS[3],
                   None,
                   BrainMonster.shadow_guardian("Guardian of Cynicism",
                                                "He thinks you are dumb.",
                                                SUMMER_WINTER_SET.shield,
                                                str(QUOTES[CAT4].pop()))
    ),
    CAT5: PoemRoom("Throne of Words",
                   "Letters and words dance around this room in glee. "
                   "This is a place of sharing and knowledge, but also "
                   "a monument to the terrible power of words.",
                   {}, POEMS[4],
                   None,
                   BrainMonster.shadow_guardian("Guardian of Words",
                                                "He sits at a desk, writing.",
                                                SUMMER_WINTER_SET.ring,
                                                str(QUOTES[CAT5].pop()))
    )
}
