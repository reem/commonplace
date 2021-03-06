"""
Jonathan Reem
January 2014

Implements Game-Ending Exceptions that can be thrown any time.
"""

from commonplace.Base import BaseObj
# pylint: disable=W0142

class GameException(Exception):
    """All game-related exceptions inherit from here.

    This allows you to do:
        isinstance(e, GameException)

    to tell where an exception came from and how to handle it.

    Special __init__ method is defined here so all Game-related
    exceptions pass their messages around in a standardized way.

    For inherited exceptions, message is defaulted to a formattable
    string which is then formatted using information provided in
    format_list. This gives maximal control to the end user while
    providing bundled defaulting for GameExceptions.
    """
    pass


class BaseVictoryException(GameException):
    """All VictoryExceptions should inherit from this class.

    Allows checking of victory conditions with:
        isinstance(e, BaseVictoryException)
    """
    pass


class BaseDefeatException(GameException):
    """All DefeatExceptions should inherit from this class."""
    pass


class PlayerDeadException(BaseDefeatException):
    """Exception raised when the Player dies to let the Game know
    for appropriate termination."""
    pass


class EnemyVictoryException(BaseDefeatException):
    """Exception raised for not defeating the enemy in time or allowing
    other enemy victory conditions to come to pass."""
    pass


class FinalBossDeadException(BaseVictoryException):
    """Exception raised when you kill the Final Boss. Causes Victory."""
    pass


class AltWinException(BaseVictoryException):
    """Victory Exception raised when the player wins by an alternate means.
    Defaults to Collecting all of some object."""
    pass


class UnhandledOptionError(Exception):
    "Thrown when an option is unhandled in a menu. Can take any arguments."
    def __init__(self, *args):
        super(UnhandledOptionError, self).__init__(
            "\n".join([arg.name if isinstance(arg, BaseObj) else arg
                       for arg in args]))


class MonsterDeadException(GameException):
    "Thrown when the monster dies in a fight."
    pass

class AbortFightException(GameException):
    "Thrown when a player runs from a fight."
    pass
