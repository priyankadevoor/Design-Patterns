from abc import ABC, abstractmethod

class LogAppender(ABC):
    @abstractmethod
    def append(self, message):
        pass

# Concrete classes impl in different files
class FileAppender(LogAppender):
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def append(self, message):
        file = open(self.file_path, 'a')
        file.write(message.get_message())
        file.close()

class ConsoleAppender(LogAppender):
    def append(self, message):
        print(message.get_message())

class DBAppender(LogAppender):
    def append(self, message):
        print("Message successfully appended to the DB - {0}".format(message.get_message()))

