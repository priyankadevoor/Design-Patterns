class Message:
    def __init__(self, content) -> None:
        self._content = content
    
    def get_content(self):
        return self._content