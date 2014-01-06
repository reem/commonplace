"""
Jonathan Reem
January 2014

Implements Game-Ending Exceptions that can be thrown any time.
"""


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
    def __init__(self, format_list, message=""):
        self.message = message.format(*format_tuple)


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
    def __init__(self, format_list, message="You were killed by {}!"):
        super(PlayerDeadException, self).__init__(format_list, message)


class EnemyVictoryException(BaseDefeatException):
    """Exception raised for not defeating the enemy in time or allowing
    other enemy victory conditions to come to pass."""
    def __init__(self, format_list,
                 message="{}'s plans came to fruition. Your cause is lost."):
        super(PlayerDeadException, self).__init__(format_list, message)


class FinalBossDeadException(BaseVictoryException):
    """Exception raised when you kill the Final Boss. Causes Victory."""
    def __init__(self, format_list,
                 message="You killed the final boss, {}!"):
        super(PlayerDeadException, self).__init__(format_list, message)


class AltWinException(BaseVictoryException):
    """Victory Exception raised when the player wins by an alternate means.
    Defaults to Collecting all of some object."""
    def __init__(self, format_list,
                 message="You collected all the {}!"):
        super(PlayerDeadException, self).__init__(format_list, message)


class UnhandledOptionError(Exception):
    def __init__(self, *args):
        self.message = "\n".join([arg.name if isinstance(arg, BaseObj) else arg
                                  for arg in args])

    def __str__(self):
        return self.message
