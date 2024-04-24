# -*- coding: utf-8 -*-
"""producer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X0PV6IETICwj5Nihc6KwQ5W7vwpEJ2Nf
"""

from kafka import KafkaProducer
import json
import time

def read_preprocessed_data(file_path):
    # Read preprocessed data from the input file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def stream_data_to_kafka(producer, topic, data):
    # Stream data to Kafka topic
    for item in data:
        producer.send(topic, json.dumps(item).encode('utf-8'))
        time.sleep(0.1)  # Adjust sleep time based on your requirements
    print("Data streaming to Kafka topic {} completed.".format(topic))

def main():
    # Kafka server configuration
    kafka_server = 'localhost:9092'

    # Kafka topic to stream data to
    kafka_topic = 'amazon_metadata_stream'

    # Preprocessed data file path
    preprocessed_data_file = 'preprocessed_data.json'

    # Initialize Kafka producer
    producer = KafkaProducer(bootstrap_servers=[kafka_server])

    # Read preprocessed data
    preprocessed_data = read_preprocessed_data(preprocessed_data_file)

    # Stream preprocessed data to Kafka topic
    stream_data_to_kafka(producer, kafka_topic, preprocessed_data)

if __name__ == "__main__":
    main()