import os
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


class KafkaProducer:
    def __init__(
        self,
        key_schema_str,
        value_schema_str,
        raw_key_model,
        raw_value_model,
        topic_name,
        header_index,
    ):
        self.topic_name = topic_name
        self.header_index = header_index
        self.key_schema = avro.loads(key_schema_str)
        self.value_schema = avro.loads(value_schema_str)
        self.avro_producer = AvroProducer(
            {
                "bootstrap.servers": os.environ["BOOTSTRAP_SERVERS"],
                "schema.registry.url": os.environ["SCHEMA_REGISTRY_URL"],
                # Safe producer settings
                # 'enable.idempotence': True,
                # High throughput
                # 'compression.type': 'snappy',
                # 'linger.ms': 20,
                # 'batch.size': 32768
            },
            default_key_schema=self.key_schema,
            default_value_schema=self.value_schema,
        )
        self.raw_key_model = raw_key_model
        self.raw_value_model = raw_value_model

    def preprocessing(self, data):
        backed_key_obj = dict()
        backed_value_obj = dict()
        for key_model in self.raw_key_model:
            key_index = self.header_index[key_model]
            backed_key_obj[key_model] = data[key_index]
        for value_model in self.raw_value_model:
            value_index = self.header_index[value_model]
            backed_value_obj[value_model] = data[value_index]
        return backed_key_obj, backed_value_obj

    def produce_event(self, data, pre_process=True):
        if pre_process == True:
            key, value = self.preprocessing(data)
        else:
            key, value = data
        self.avro_producer.produce(topic=self.topic_name, key=key, value=value)
        self.avro_producer.poll(0.1)

    # def delivery_report(err, msg):
    #     """ Called once for each message produced to indicate delivery result.
    #         Triggered by poll() or flush(). """
    #     if err is not None:
    #         print('Message delivery failed: {}'.format(err))
    #     else:
    #         print('Message delivered to {} [{}]'.format(
    #             msg.topic(), msg.partition()))
