from Topic import Topic
from Publisher import Publisher
from Message import Message
from ConcreteSubscriber import ConcreteSubscriber

class PubSubService:
    def __init__(self) -> None:
        self._topics = {}

    def create_topic(self, topic_name):
        if topic_name not in self._topics.keys():   
            self._topics[topic_name] = Topic(topic_name)

    def subscribe(self, topic_name, subscriber):
        if topic_name in self._topics.keys():
            topic = self._topics[topic_name]
            topic.add_subscriber(subscriber)
    
    def unsubscribe(self, topic_name, subscriber):
        if topic_name in self._topics.keys():
            topic = self._topics[topic_name]
            topic.remove_subscriber(subscriber)

    def publish(self, topic_name, message):
        if topic_name in self._topics.keys():
            topic = self._topics[topic_name]
            topic.publish(message)

    def get_topics(self):
        topics = []
        for key, topic in self._topics.items():
            topics.append(topic.get_topic_name())
        return topics

pubsubservice = PubSubService()
pubsubservice.create_topic('Sports')
pubsubservice.create_topic('Weather')
pubsubservice.create_topic('News')

pub1 = Publisher('Sports')
pub2 = Publisher('Weather')
pub3 = Publisher('News')

s1 = ConcreteSubscriber('Priya')
s2 = ConcreteSubscriber('Shiv')

pubsubservice.subscribe('Sports', s1)
pubsubservice.subscribe('Weather', s1)
pubsubservice.subscribe('News', s1)

pubsubservice.subscribe('Weather', s2)
pubsubservice.subscribe('News', s2)

pubsubservice.publish('Sports', Message('RCB won the IPL cup in 2025!'))
pubsubservice.publish('Weather', Message('Charlotte weather is great today!'))
pubsubservice.publish('News', Message('India"s GPD Increased '))

pubsubservice.unsubscribe('News', s2)

pubsubservice.publish('Sports', Message('RCB won the IPL cup in 2025!'))
pubsubservice.publish('Weather', Message('Charlotte weather is great today!'))
pubsubservice.publish('News', Message('India"s GPD Increased '))

print(pubsubservice.get_topics())



