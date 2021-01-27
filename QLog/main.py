""" main """

import QLog
from QLog.console_logger import ConsoleLogger
from QLog import QLogHighlight, QLogDebug, QLogInfo, QLogWarning, QLogError


def main():
    """ main """

    QLog.loggers = [ConsoleLogger()]
    QLogHighlight('Highlight')
    QLogDebug('Debug')
    QLogInfo('Info')
    QLogWarning('Warning')
    QLogError('Error')


if __name__ == '__main__':
    main()
