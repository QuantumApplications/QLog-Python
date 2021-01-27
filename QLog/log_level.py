""" The enum defining the log levels """

from enum import Enum


class LogLevel(Enum):
    """ The enum defining the log levels """

    highlight = 4
    debug = 3
    info = 2
    warning = 1
    error = 0

    @property
    def ansi_color(self):
        """ Associates an ansi color with each log level """

        return ansi_colors[self]

    @property
    def ansi_color_sequence(self):
        """ Returns ANSI color sequence """

        return u'\u001b' + '[' + str(self.ansi_color)

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            # pylint: disable=W0143
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            # pylint: disable=W0143
            return self.value <= other.value
        return NotImplemented


ansi_colors = {
    LogLevel.highlight: '35m',
    LogLevel.debug: '34m',
    LogLevel.info: '32m',
    LogLevel.warning: '33m',
    LogLevel.error: '31m'
}
