class LogConfig:
    def __init__(self, log_level, log_appender) -> None:
        self._log_level = log_level
        self._log_appender = log_appender

    def set_log_level(self, log_level):
        self._log_level = log_level

    def get_log_level(self):
        return self._log_level
    
    def set_log_appender(self, log_appender):
        self._log_appender = log_appender

    def get_log_appender(self):
        return self._log_appender