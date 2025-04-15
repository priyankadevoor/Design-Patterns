class Topic:
    def __init__(self, topic_name) -> None:
        self._name = topic_name
        self._subscribers = set()
    
    def get_topic_name(self):
        return self._name
    
    def get_subscribers(self):
        return self._subscribers
    
    def add_subscriber(self, subscriber):
        self._subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
    
    def publish(self, message):
        for subscriber in self._subscribers:
            subscriber.on_message(message)

            
