# KAFKA

## Kafka Initalizing

    1. Download binary version of kafka from https://kafka.apache.org/downloads.
    2. Export kafka PATH to ~/.bachrc.
        - Example: export PATH=/PATH_OF_KAFKA_FILE_EXTRACTED/kafka_2.11-2.4.0/bin:$PATH
    3. Make a directory called __data__ in kafka directory
        - Make two directories called __kafka__ and __zookeeper__ in __data__ directory
    4. Change dataDir in __/config/zookeeper.properties__ to __/data/zookeeper__ directory 
    5. Change dataDir in __/config/server.properties__ to __/data/kafka__

## Running Kafka

    1. Run Zookeeper
        - __/bin/zookeeper-server-start.sh config/zookeeper.properties__
    2. Run Kafka
        - __/bin/kafka-server-start.sh config/server.propertires__

## "kafka-topics.sh" commands
>
> ##### craeting a topic 
>
> kafka-topics.sh --zookeeper 127.0.0.1:2181 --topic TOPIC_NAME --create --partitions NUM_OF_PARTITIONS --replication-factor NUM_OF_REPLICATIONS
>
> ##### list of topics
>
> kafka-topics.sh --zookeeper 127.0.0.1:2181 --list
>
> ##### describe a topic
>
> kafka-topics.sh --zookeeper 127.0.0.1:2181 --topic NAME_OF_TOPIC --describe
>
> ##### delete a topic
>
> kafka-topics.sh --zookeeper 127.0.0.1:2181 --topic NAME_OF_TOPIC --delete

## "kafka-console-producer.sh" commands
>
> ##### produce a message
>
> kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic TOPIC_NAME
>
> ##### produce messsage with properties
>
> kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic TOPIC_NAME --producer-property acks=all

## "kafka-console-consumer.sh" commands
>
> ##### consume a message
>
> kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic TOPIC_NAME
>
> ##### consume messages from begining
>
> kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic TOPIC_NAME --from-begining
>
> ##### create a group odf consumers
>
> kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic TOPIC_NAME --group GROUP_NAME

## "kafka-consumer-groups.sh" commands
>
> ##### list of consumer groups
>
> kafka-consumer-groups.sh --bootstrap-server 127.0.0.1:9092 --list
>
> ##### describe a group
>
> kafka-consumer-groups.sh --bootstrap-server 127.0.0.1:9092 --describe --group GROUP_NAME
