from datetime import datetime
class LogMessage:
    def __init__(self, log_level, message):
        self._log_level = log_level
        self._message = message
        self._timestamp = datetime.now()
    
    def get_message(self):
        return self._message
    
    def get_timestamp(self):
        return self._timestamp
    
    def get_level(self):
        return self._log_level
    