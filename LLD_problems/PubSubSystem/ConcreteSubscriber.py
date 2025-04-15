class ConcreteSubscriber:
    def __init__(self, name) -> None:
        self._name = name

    def on_message(self, message):
        print(message.get_content())