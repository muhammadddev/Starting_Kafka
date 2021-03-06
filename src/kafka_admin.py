import os
from confluent_kafka.admin import AdminClient, NewTopic


class KafkaAdmin:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.admin_client = AdminClient({"bootstrap.servers": ""})

    def create_topic(self):
        new_topic = NewTopic(self.topic_name, num_partitions=1, replication_factor=1,)
        fs = self.admin_client.create_topics([new_topic])

        for topic, f in fs.items():
            try:
                f.result()
                print("Topic {} created".format(topic))
                return True
            except Exception as e:
                print("Failed to create topic {}: {}".format(topic, e))
                return False
