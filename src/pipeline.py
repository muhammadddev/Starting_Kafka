from src.config_manager import ConfigManager
from src.kafka_admin import KafkaAdmin
from src.kafka_producer import KafkaProducer
from src.schema_registry import SchemaRegistry


class Pipeline:
    def __init__(self, path_to_config):
        self.config_obj = ConfigManager.from_yaml(path_to_config)
        self.topic_name = "{}_event_stream".format(self.config_obj.get_project_name())
        self.kafka_topic = KafkaAdmin(self.topic_name).create_topic()
        self.schema_obj = SchemaRegistry(
            self.config_obj.get_project_name(), self.config_obj.get_column_list()
        )
        self.kafka_producer = KafkaProducer(
            self.schema_obj.key_schema(),
            self.schema_obj.value_schema(),
            self.config_obj.get_key_shape(),
            self.config_obj.get_value_shape(),
            self.topic_name,
            self.config_obj.generate_column_map(),
        )

    def insert(self, data):
        self.kafka_producer.produce_event(data)
