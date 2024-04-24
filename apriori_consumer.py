# -*- coding: utf-8 -*-

import json
from kafka import KafkaConsumer

# Function to generate candidate itemsets of size k from frequent itemsets of size k-1
def generate_candidate_itemsets(prev_itemsets, k):
    candidate_itemsets = set()
    for i in range(len(prev_itemsets)):
        for j in range(i+1, len(prev_itemsets)):
            itemset1 = prev_itemsets[i]
            itemset2 = prev_itemsets[j]
            if itemset1[:-1] == itemset2[:-1]:  # Check if first k-2 elements are equal
                new_itemset = tuple(sorted(set(itemset1) | set(itemset2)))
                candidate_itemsets.add(new_itemset)
    return candidate_itemsets

# Function to prune candidate itemsets based on frequent itemsets of size k-1
def prune_candidate_itemsets(candidate_itemsets, prev_itemsets):
    pruned_itemsets = set()
    for itemset in candidate_itemsets:
        subsets = [itemset[:i] + itemset[i+1:] for i in range(len(itemset))]  # Generate all possible subsets
        if all(subset in prev_itemsets for subset in subsets):  # Check if all subsets are frequent
            pruned_itemsets.add(itemset)
    return pruned_itemsets

# Function to find frequent itemsets using Apriori algorithm
def apriori(transaction_data, min_support):
    item_counts = {}  # Dictionary to store counts of individual items
    num_transactions = len(transaction_data)
    frequent_itemsets = []
    k = 1

    # Initialize item counts
    for transaction in transaction_data:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    # Generate frequent itemsets of size 1
    frequent_itemsets.append([item for item, count in item_counts.items() if count / num_transactions >= min_support])
    while frequent_itemsets[-1]:  # Continue until no frequent itemsets are found
        prev_itemsets = frequent_itemsets[-1]
        k += 1
        candidate_itemsets = generate_candidate_itemsets(prev_itemsets, k)
        candidate_item_counts = {itemset: 0 for itemset in candidate_itemsets}

        # Count occurrences of candidate itemsets in transactions
        for transaction in transaction_data:
            for candidate_itemset in candidate_itemsets:
                if set(candidate_itemset).issubset(set(transaction)):
                    candidate_item_counts[candidate_itemset] += 1

        # Prune candidate itemsets that do not meet minimum support
        frequent_itemsets.append([itemset for itemset, count in candidate_item_counts.items() if count / num_transactions >= min_support])

    return frequent_itemsets[:-1]  # Remove last itemset as it is empty

# Load Kafka consumer
consumer = KafkaConsumer('preprocessed_data', bootstrap_servers=['localhost:9092'], group_id='apriori_consumer')

# Initialize variables
transactions = []
min_support = 0.1  # Set minimum support threshold

# Consume messages from Kafka topic and process transactions
try:
    for message in consumer:
        data = json.loads(message.value.decode('utf-8'))
        transactions.append(data['transaction'])

        # Run Apriori algorithm when a sufficient number of transactions are collected
        if len(transactions) >= 100:
            frequent_itemsets = apriori(transactions, min_support)
            print("Frequent Itemsets:")
            for itemset in frequent_itemsets:
                print(itemset)
            transactions = []  # Reset transactions
except Exception as e:
    print("An error occurred:", str(e))
finally:
    consumer.close()
