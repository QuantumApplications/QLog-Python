""" LogEntry tests """
from datetime import datetime

from QLog import LogLevel, LogEntry


def test_log_entry():
    """ Test meta text """

    # 1. Arrange
    date = datetime.now()
    file = 'file'
    function = 'function'
    line = 1
    level = LogLevel.error
    data = 'data'

    entry = LogEntry(
        date,
        file,
        function,
        line,
        level,
        data
    )

    # 3. Assert
    assert entry.meta_text == str(date) + ': ' + file + ':' + str(line) + ' ' + function + ': '
