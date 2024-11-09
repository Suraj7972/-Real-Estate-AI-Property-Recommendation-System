import numpy as np

# Function to calculate Mean Average Precision (MAP)
def calculate_map(actual, predicted):
    avg_precision = 0.0
    num_correct_predictions = 0
    
    for i, pred in enumerate(predicted):
        if pred in actual:
            num_correct_predictions += 1
            precision_at_k = num_correct_predictions / (i + 1)
            avg_precision += precision_at_k
    
    if not actual:
        return 0.0
    
    return avg_precision / len(actual)

# Example of usage
# Assuming you have a test set with actual property indices and the corresponding predicted indices
actual_indices = [1, 3, 5]
predicted_indices = [1, 2, 3, 4, 5]

map_score = calculate_map(actual_indices, predicted_indices)
print(f'Mean Average Precision: {map_score}')
