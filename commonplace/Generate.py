"""
Jonathan Reem
January 2014

Generates all game objects.
"""

import commonplace.Items as Items

QUOTE_FILE = 'quotes.txt'
QUOTES = read_quotes(QUOTE_FILE)
# pylint: disable=R0903, R0913


class Quote(object):
    "Holds a quote for generation purposes."
    def __init__(self, text, author, category):
        self.text = text
        self.author = author
        self.category = category

    def __str__(self):
        "Translating from a Quote object to a string. Loses category."
        return "{0.text}\n    -- {0.author}".format(self)


def read_quotes(quote_filename):
    """Reads the quotes from a file.

    File format as follows:

    Categories:
        Category 1
        Category 2
        Category 3

    Quotes:

    1
    Text:
    Quote Text One
    Author:
    Author1
    Category:
    Category of Quote1

    2
    Text:
    Quote Text Two
    Author:
    Author2
    Category:
    Category of Quote2

    Parses to a dictionary of {category: [Quote]}

    See the Quote class.
    """
    with open(quote_filename, 'r') as quote_file:
        raw_quotes = quote_file.readlines()

    categories = set()

    line_num = 0
    assert raw_quotes[line_num] == 'Categories:\n'
    line_num += 1
    while raw_quotes[line_num][0:4] == '    ':
        categories.add(raw_quotes[line_num].strip()[4:])
        line_num += 1

    quotes = {category: [] for category in categories}

    line_num += 1  # Swallow \n between Categories and Quotes:
    assert raw_quotes[line_num] == 'Quotes:\n'

    current_quote_num = 1
    while line_num != len(raw_quotes) - 1:
        current_quote_str = str(current_quote_num) + '\n'
        while raw_quotes[line_num] != current_quote_str:
            line_num += 1

        line_num += 1  # go to Text:
        assert raw_quotes[line_num] == 'Text:\n'
        line_num += 1  # Advance to quote text

        quote_text = ''
        while raw_quotes[line_num] != 'Author:\n':
            quote_text += raw_quotes[line_num]

        # Ensure that we haven't reached the end of the file or something.
        assert raw_quotes[line_num] == 'Author:\n'
        line_num += 1  # Advance to author text
        author = raw_quotes[line_num].strip()

        line_num += 1  # Advance to Category:\n
        assert raw_quotes[line_num] == 'Category:\n'
        line_num += 1  # Adance to category text

        category = raw_quotes[line_num].strip()
        assert category in categories

        quotes[category].append(Quote(quote_text, author, category))
        current_quote_num += 1


def generate_all():
    "Generates a player and map."
    return (generate_player(), generate_map())


def generate_player():
    "Generates a player."
    pass


def generate_map():
    "Generates a map."
    pass


def generate_monster(monster_template):
    "Generates a monster from a monster_template"
    pass


class MonsterTemplate(object):
    "Template to generate a monster."
    def __init__(self, name, description, category, strength):
        self.name = name
        self.description = description
        self.category = category
        self.strength = strength


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
    Items.BrainEquipment(
        "Sword of Invincible Summer", "The sword glows a fiery red.",
        'weapon', {'health': -500, 'attack': 2000},
        "... I found there was, within me, an invincible summer."
        "\n    - Albert Camus"),

    Items.BrainEquipment(
        "Helmet of Winter", "The helmet is cold and heavy, but unblemished.",
        'helmet', {'health': 250, 'attack': -50},
        "In the midst of Winter ...\n    - Albert Camus"),

    Items.BrainEquipment(
        "Shield of Winter", "The shield is cold and heavy, but unblemished.",
        'shield', {'health': 500, 'attack': -100},
        "In the midst of Winter ...\n    - Albert Camus"),

    Items.BrainEquipment(
        "Armor of Winter",
        "The armor is cold and extremely heavy, but unblemished.",
        'armor', {'health': 1000, 'attack': -200},
        "In the midst of Winter ...\n    - Albert Camus"),

    Items.BrainEquipment(
        "Ring of Winter",
        "The ring is frighteningly cold and exudes an aura of protection.",
        'armor', {'health': 500, 'attack': -100},
        "In the midst of Winter ...\n    - Albert Camus"))
