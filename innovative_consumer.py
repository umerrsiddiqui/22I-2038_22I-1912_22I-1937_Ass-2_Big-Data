# -*- coding: utf-8 -*-
"""innovative_consumer

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X0PV6IETICwj5Nihc6KwQ5W7vwpEJ2Nf
"""

import json
from kafka import KafkaConsumer
import matplotlib.pyplot as plt

def process_data(record):
    # Process the received data record
    data = json.loads(record.value.decode('utf-8'))

    # Implement your innovative analysis here
    # Example: Calculate sentiment score from product descriptions

    # Extract product description
    description = data.get('description', '')

    # Perform sentiment analysis (dummy implementation)
    sentiment_score = len(description.split())  # Example: Count words in description

    return sentiment_score

def visualize_data(sentiment_scores):
    # Visualize the sentiment scores
    plt.figure(figsize=(10, 6))
    plt.hist(sentiment_scores, bins=20, color='skyblue', edgecolor='black')
    plt.title('Sentiment Analysis of Product Descriptions')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def run_consumer():
    # Kafka Consumer settings
    consumer = KafkaConsumer('preprocessed_data', bootstrap_servers=['localhost:9092'])

    # Initialize sentiment scores list
    sentiment_scores = []

    try:
        # Start consuming messages
        for record in consumer:
            # Process the data record
            sentiment_score = process_data(record)

            # Add sentiment score to the list
            sentiment_scores.append(sentiment_score)

            # Visualize data periodically
            if len(sentiment_scores) % 100 == 0:
                visualize_data(sentiment_scores)

    except KeyboardInterrupt:
        # Handle keyboard interrupt
        consumer.close()

if __name__ == "__main__":
    run_consumer()