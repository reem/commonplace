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
        result = ""
        for info_attribute in ("name", "description"):
            result += "{!r}\n".format(getattr(self, info_attribute))
        return result

    def __str__(self):
        result = ""
        for info_attribute in ("name, description"):
            result += "{!s}\n".format(getattr(self, info_attribute))
        return result
