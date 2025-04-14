class User:
    def __init__(self, name, email) -> None:
        self._name = name
        self._email = email
    
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email