class Publisher:
    def __init__(self, topic) -> None:
        self._topic = topic

    def publish(self, message):
        self._topic.publish(message)