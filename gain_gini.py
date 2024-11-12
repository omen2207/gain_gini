import csv
import math
def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  
        for row in csv_reader:
            data.append(row)
    return headers, data
def count_labels(data):
    label_counts = {}
    for row in data:
        label = row[-1]  
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    return label_counts
def calculate_entropy(data):
    total = len(data)
    label_counts = count_labels(data)
    entropy = 0.0
    for label in label_counts:
        prob = label_counts[label] / total
        entropy -= prob * math.log2(prob)  
    return entropy
def calculate_gini_index(data):
    total = len(data)
    label_counts = count_labels(data)
    gini = 1.0
    for label in label_counts:
        prob = label_counts[label] / total
        gini -= prob ** 2 
    return gini
def split_data_by_attribute(data, attribute_index):
    subsets = {}
    for row in data:
        attribute_value = row[attribute_index]
        if attribute_value in subsets:
            subsets[attribute_value].append(row)
        else:
            subsets[attribute_value] = [row]
    return subsets
def information_gain(data, attribute_index):
    total_entropy = calculate_entropy(data)
    subsets = split_data_by_attribute(data, attribute_index)
    weighted_entropy = 0.0
    total_instances = len(data)
    for subset in subsets.values():
        prob = len(subset) / total_instances
        weighted_entropy += prob * calculate_entropy(subset)

    gain = total_entropy - weighted_entropy
    return gain
def gini_index_for_attribute(data, attribute_index):
    subsets = split_data_by_attribute(data, attribute_index)
    weighted_gini = 0.0
    total_instances = len(data)
    for subset in subsets.values():
        prob = len(subset) / total_instances
        weighted_gini += prob * calculate_gini_index(subset)

    return weighted_gini
headers, data = read_csv(r'C:\Users\bhilw\OneDrive\Documents\DM\12_Gain_gini\data.csv')
print("Attribute Information Gain and Gini Index:")
for i in range(len(headers) - 1):  
    print(f"\nAttribute: {headers[i]}")
    gain = information_gain(data, i)
    gini = gini_index_for_attribute(data, i)
    print(f"Information Gain: {gain}")
    print(f"Gini Index: {gini}")
