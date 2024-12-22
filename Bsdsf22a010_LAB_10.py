import pandas as pd
import numpy as np
from collections import Counter
from math import log2
def calculate_entropy(data, target_col):
    values = data[target_col].value_counts(normalize=True)
    return -sum(value * log2(value) for value in values)
def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    values, counts = np.unique(data[attribute], return_counts=True)
    weighted_entropy = sum(
        (counts[i] / sum(counts)) * calculate_entropy(data[data[attribute] == values[i]], target_col)
        for i in range(len(values))
    )
    return total_entropy - weighted_entropy
def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    if len(np.unique(data[target_col])) == 1:
        return np.unique(data[target_col])[0]
    if len(attributes) == 0 or depth >= max_depth:
        return Counter(data[target_col]).most_common(1)[0][0]
    
    gains = {attr: calculate_information_gain(data, attr, target_col) for attr in attributes}
    best_attr = max(gains, key=gains.get)

    tree = {best_attr: {}}
    attributes = [attr for attr in attributes if attr != best_attr]

    for value in np.unique(data[best_attr]):
        subset = data[data[best_attr] == value]
        subtree = build_tree(subset, attributes, target_col, depth + 1, max_depth)
        tree[best_attr][value] = subtree
    
    return tree
def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree
    root_attr = next(iter(tree))
    value = data_point[root_attr]
    if value not in tree[root_attr]:
        return None 
    return predict(tree[root_attr][value], data_point)
def build_random_forest(data, attributes, target_col, n_trees=2, max_depth=3):
    trees = []
    n_samples = len(data)

    for _ in range(n_trees):
        bootstrap_sample = data.sample(n=n_samples, replace=True)
        random_attributes = np.random.choice(attributes, size=int(np.sqrt(len(attributes))), replace=False)
        tree = build_tree(bootstrap_sample, random_attributes, target_col, max_depth=max_depth)
        trees.append(tree)
    
    return trees
def random_forest_predict(forest, data_point):
    predictions = [predict(tree, data_point) for tree in forest]
    return Counter(predictions).most_common(1)[0][0]

if __name__ == "__main__":
    data = pd.DataFrame({
        'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
        'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
        'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    })
    
    target_col = 'PlayTennis'
    attributes = [col for col in data.columns if col != target_col]
    tree = build_tree(data, attributes, target_col, max_depth=3)
    print("Decision Tree:", tree)
    data_point = {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Weak'}
    print("Single Tree Prediction:", predict(tree, data_point))
    forest = build_random_forest(data, attributes, target_col, n_trees=3, max_depth=3)
    print("Random Forest Prediction:", random_forest_predict(forest, data_point))
