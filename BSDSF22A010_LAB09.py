import math
from collections import Counter
import pandas as pd

def calculate_entropy(data, target_col):
    target_counts = Counter(data[target_col])
    total_instances = len(data[target_col])
    entropy = 0
    for count in target_counts.values():
        probability = count / total_instances
        entropy -= probability * math.log2(probability)
    return entropy

def calculate_information_gain(data, attribute, target_col):
    parent_entropy = calculate_entropy(data, target_col)
    total_instances = len(data)
    weighted_entropy = 0
    for value in set(data[attribute]):
        subset = data[data[attribute] == value]
        subset_entropy = calculate_entropy(subset, target_col)
        weighted_entropy += (len(subset) / total_instances) * subset_entropy
    information_gain = parent_entropy - weighted_entropy
    return information_gain

def build_tree(data, attributes, target_col):
    if len(set(data[target_col])) == 1:
        return data[target_col].iloc[0]
    if not attributes:
        return data[target_col].mode()[0]
    best_attribute = max(attributes, key=lambda attr: calculate_information_gain(data, attr, target_col))
    tree = {best_attribute: {}}
    for value in set(data[best_attribute]):
        subset = data[data[best_attribute] == value]
        if subset.empty:
            tree[best_attribute][value] = data[target_col].mode()[0]
        else:
            remaining_attributes = [attr for attr in attributes if attr != best_attribute]
            tree[best_attribute][value] = build_tree(subset, remaining_attributes, target_col)
    return tree

def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree
    attribute = list(tree.keys())[0]
    value = data_point.get(attribute)
    subtree = tree[attribute].get(value)
    if subtree is None:
        return None
    return predict(subtree, data_point)

if __name__ == "__main__":
    data = pd.DataFrame({
        "Weather": ["Sunny", "Overcast", "Rainy"],
        "Temperature": ["Hot", "Hot", "Mild"],
        "Play": ["No", "Yes", "Yes"]
    })

    target_col = "Play"
    attributes = ["Weather", "Temperature"]

    tree = build_tree(data, attributes, target_col)
    print("Decision Tree:", tree)

    test_data_point = {"Weather": "Sunny", "Temperature": "Hot"}
    prediction = predict(tree, test_data_point)
    print("Prediction for", test_data_point, ":", prediction)

