""" QLog tests """
import QLog
from QLog import LogLevel, log
from QLog.test.mock_logger import MockLogger


def test_log_string():
    """ Test logging string """

    # 1. Arrange
    mock_logger = MockLogger()
    QLog.loggers = [mock_logger]
    data = 'a'

    # 2. Action
    log(LogLevel.ERROR, data)

    # 3. Assert
    assert mock_logger.log_entry.text == str(data)


def test_log_int():
    """ Test logging int """

    # 1. Arrange
    mock_logger = MockLogger()
    QLog.loggers = [mock_logger]
    data = 1

    # 2. Action
    log(LogLevel.ERROR, data)

    # 3. Assert
    assert mock_logger.log_entry.text == str(data)


def test_log_array():
    """ Test logging array """

    # 1. Arrange
    mock_logger = MockLogger()
    QLog.loggers = [mock_logger]
    data = [1]

    # 2. Action
    log(LogLevel.ERROR, data)

    # 3. Assert
    assert mock_logger.log_entry.text == str(data)
