"""
Jonathan Reem
Implements a very basic template for eliminating boilerplate code elsewhere
"""

# pylint: disable=R0903

from operator import eq

class BaseObj(object):
    """
    Base Object that implements a basic str and repr as well as mandating
    name and description.
    """

    def __init__(self, name, description):
        """
        Gets name and description attributes.
        name: name of the object
        description: a description of the object
        """
        self.name = name
        self.description = description

    def __repr__(self):
        return "{0.name!r}    {0.description!r}".format(self)

    def __str__(self):
        return "{0.name}\n{0.description}".format(self)


def format_objects(items, indent=1):
    "Formats lists or dictionaries for pretty printing."
    if isinstance(items, list):
        return "\n".join(["    " * indent + "{0}. {1.name}".format(i + 1, item)
                          for i, item in enumerate(items)])
    elif isinstance(items, dict):
        try:
            return "\n".join(["    " * indent + "{k}: {v}".format(
                k=k, v=items[k].name if items[k] is not None else 'None')
                              for k in items])
        except AttributeError:
            return "\n".join(["    " * indent + "{k}: {v}".format(
                k=k, v=items[k]) for k in items])
    else:
        raise TypeError(type(items))


def spaced_print(string, pre=True, post=True):
    "Prints with spaces."
    print "{0}{1}{2}".format('\n' if pre else '',
                             string,
                             '\n' if post else '')

def bumped_range(stop):
    "Range for non computer scientists (aka for prompting)."
    return range(1, stop+1)

def assert_with_dump(*args, **kwargs):
    "Passes the arguments to the keyword arg callback. Prints args if not true."
    callback = kwargs.get('callback', eq)

    try:
        assert callback(*args)
    except AssertionError:
        for arg in args:
            print arg
        raise
