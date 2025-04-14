"""
Main features - 
1. Should be able to log message to a file, console or a database.
2. LogMessages could be of 5 types.
3. Should provide way to change log level and logging output type.
"""
"""
Entities -
LogLevel -
    Enum:
    INFO - 1
    DEBUG - 2
    WARN - 3
    ERROR - 4
    FATAL - 5
LogMessage - 
    attr:
        - level
        - message
        - logged_timestamp
    methods:
        - get_level()
        - get_message()
        - get_timestamp()
LogConfig - 
    attr:
        - log_level
        - log_output
    methods:
        - set_logconfig()
        - get_logconfig()
LogAppender -
    @abstract_method
    append()
3 Concrete classes
    - FileAppender
        append()
    - DBAppender
        append()
    - ConsoleAppender
        append()
LoggingFramework
    attr:

    methods:
        - set_config()
        - log_message()


"""
from LogLevel import LogLevel
from LogMessage import LogMessage
from LogConfig import LogConfig
from LogAppender import FileAppender, ConsoleAppender

class LoggingFramework:
    def __init__(self, config):
        self.config = config

    def set_config(self, config):
        self.config = config

    def log(self, level, message):
        msg = LogMessage(level, message)
        appender = self.config.get_log_appender()
        appender.append(msg)

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def debug(self, message):
        self.log(LogLevel.DEBUG, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)

    def warn(self, message):
        self.log(LogLevel.WARN, message)

    def fatal(self, message):
        self.log(LogLevel.FATAL, message)
    

config = LogConfig(LogLevel.INFO, FileAppender('app.txt'))
logging = LoggingFramework(config)
logging.info('GPS is working fine.')
config.set_log_appender(ConsoleAppender())
logging.debug('GPS data lat is:,\n longitude is:')