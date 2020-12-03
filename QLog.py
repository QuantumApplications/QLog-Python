import inspect
import os
from datetime import datetime

from log_entry import LogEntry
from log_level import LogLevel
from logger import Logger


def QLogHighlight(data):
    QLog.log(LogLevel.highlight, data)

def QLogDebug(data):
    QLog.log(LogLevel.debug, data)

def QLogInfo(data):
    QLog.log(LogLevel.info, data)

def QLogWarning(data):
    QLog.log(LogLevel.warning, data)

def QLogError(data):
    QLog.log(LogLevel.error, data)


class QLog:
    loggers: [Logger] = []

    @staticmethod
    def log(log_level: LogLevel, data):
        caller = inspect.stack()[2]
        log_entry = LogEntry(
            datetime.now(),
            os.path.splitext(os.path.basename(caller.filename))[0],
            caller.function,
            caller.lineno,
            log_level,
            data
        )
        for logger in QLog.loggers:
            logger.log(log_entry)
