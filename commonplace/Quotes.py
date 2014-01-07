"""
Jonathan Reem
January 2014

Extracts and exports Quotes
"""

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
        categories.add(raw_quotes[line_num].strip())
        line_num += 1

    quotes = {category: [] for category in categories}

    line_num += 1  # Swallow \n between Categories and Quotes:
    assert raw_quotes[line_num] == 'Quotes:\n'

    current_quote_num = 1
    while line_num < len(raw_quotes) - 1:
        line_num += 1
        current_quote_str = str(current_quote_num) + '\n'
        while raw_quotes[line_num] != current_quote_str:
            line_num += 1

        line_num += 1  # go to Text:
        assert raw_quotes[line_num] == 'Text:\n'
        line_num += 1  # Advance to quote text

        quote_text = ''
        while raw_quotes[line_num] != 'Author:\n':
            quote_text += raw_quotes[line_num]
            line_num += 1

        # Ensure that we haven't reached the end of the file or something.
        assert raw_quotes[line_num] == 'Author:\n'
        line_num += 1  # Advance to author text
        author = raw_quotes[line_num].strip()

        line_num += 1  # Advance to Category:\n
        assert raw_quotes[line_num] == 'Category:\n'
        line_num += 1  # Advance to category text

        category = raw_quotes[line_num].strip()
        assert category in categories

        quotes[category].append(Quote(quote_text, author, category))
        current_quote_num += 1

    return categories, quotes

QUOTE_FILE = './commonplace/quotes.txt'
CATEGORIES, QUOTES = read_quotes(QUOTE_FILE)
