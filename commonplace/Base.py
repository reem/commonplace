"""
Jonathan Reem
Implements a very basic template for eliminating boilerplate code elsewhere
"""

__all__ = ["BaseObj"]


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
