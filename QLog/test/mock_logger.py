"""  Mocked logger for testing """

from QLog.log_entry import LogEntry
from QLog.log_level import LogLevel
from QLog.logger import Logger


class MockLogger(Logger):
    """  Mocked logger for testing """

    log_entry: LogEntry = None

    def __init__(self, log_level=LogLevel.highlight):
        self.log_level = log_level

    def do_log(self, log_entry: LogEntry):
        self.log_entry = log_entry
