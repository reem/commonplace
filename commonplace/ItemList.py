"""
Creates and exports the ITEMS dict.

Items is of the form:
    category: {strength: ItemTemplate}
"""

from commonplace.Quotes import CATEGORIES
from commonplace.Base import bumped_range
from random import shuffle
# pylint: disable=R0903,R0913


class ItemTemplate(object):
    "Template to generate an item."
    def __init__(self, name, description, category, strength, item_type):
        self.name = name
        self.description = description
        self.category = category
        self.strength = strength
        self.item_type = item_type


def create_items_from_file(item_filename):
    """
    Creates an items dict of the form in the module docstring
    from a file of the form:

    Types:
        Helmet
        Armor
        Sword
        Shield
        Ring

    1
    Name:
    Name of Item 1
    Description:
    Description of Item 1
    Category:
    Category of Item 1
    Strength: Num_Strength (1-4)
    Type:
    Type of Item 1

    2
    Name:
    Name of Item 2
    Description:
    Description of Item 2
    Category:
    Category of Item 2
    Strength: Num_Strength (1-4)
    Type:
    Type of Item 2

    etc.
    """
    with open(item_filename, 'r') as item_file:
        raw_items = item_file.readlines()

    items = {category: {strength: [] for strength in bumped_range(4)}
             for category in CATEGORIES}

    line_num = 0
    current_item_num = 1

    types = set()

    assert raw_items[line_num] == 'Types:\n'
    line_num += 1

    while raw_items[line_num][0:4] == '    ':
        types.add(raw_items[line_num].strip())
        line_num += 1

    line_num += 1  # Swallow \n between sections

    while line_num < len(raw_items) - 1:

        current_item_num_str = str(current_item_num) + '\n'
        assert current_item_num_str == raw_items[line_num]

        line_num += 1  # Advance to Name:\n
        assert raw_items[line_num] == 'Name:\n'

        line_num += 1  # Advance to Name text
        name = raw_items[line_num].strip()

        line_num += 1  # Advance to Description:\n
        assert raw_items[line_num] == 'Description:\n'

        line_num += 1  # Advance to Description text.
        description = ''
        while raw_items[line_num] != 'Category:\n':
            description += raw_items[line_num].strip() + ' '
            line_num += 1

        assert raw_items[line_num] == 'Category:\n'

        line_num += 1  # Advance to Category text
        category = raw_items[line_num].strip()
        assert category in CATEGORIES

        line_num += 1  # Advance to Strength: Num\n
        assert raw_items[line_num][0:10] == 'Strength: '

        try:
            strength = int(raw_items[line_num].strip()[10:])
        except ValueError:
            print raw_items[line_num]
            raise

        line_num += 1  # Advance to Type:\n
        assert raw_items[line_num] == 'Type:\n'

        line_num += 1  # Advance to Type Text
        item_type = raw_items[line_num].strip()
        assert item_type in types

        line_num += 2

        current_item_num += 1
        new_item = ItemTemplate(name, description, category,
                                strength, item_type)
        items[category][strength].append(new_item)

    for _, i in items.iteritems():
        for _, j in i.iteritems():
            shuffle(j)
    return items

ITEM_FILE = "./commonplace/items.txt"
ITEMS = create_items_from_file(ITEM_FILE)
