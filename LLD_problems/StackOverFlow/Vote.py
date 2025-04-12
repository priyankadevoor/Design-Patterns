class Vote:
    def __init__(self, value) -> None:
        self.id = id(self)
        self.value = value

    def get_value(self):
        return self.value
