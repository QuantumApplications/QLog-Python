"""  Logger abstract class """

from abc import ABC, abstractmethod

from log_entry import LogEntry
from log_level import LogLevel


class Logger(ABC):
    """  Logger abstract class """

    log_level: LogLevel

    @abstractmethod
    def do_log(self, log_entry):
        """ Log function to implement """

        pass

    def log(self, log_entry: LogEntry):
        """ Log function to use """

        if log_entry.log_level <= self.log_level:
            self.do_log(log_entry)
