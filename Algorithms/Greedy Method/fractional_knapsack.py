## Basic fractional knapsack implementation

# Steps
# 1. Calculate the ratio: For each item, calculate the ratio of value to weight (v_i/w_i)
# 2. Sort the Items: Sort the items based on their value-to-weight ratio in descending order
# 3. Fill Knapsack: Starting with the highest ratio item, add items or fractions  to the knapsack until capacity

def fractionalKnapsack(S, W):
    # Step 1/2
    S.sort(key = lambda x: x[1]/x[0], reverse = True)
    
    total_value = 0
    total_weight = 0
    
    result = [0] * len(S)
    
    # Step 3
    for i, (weight, value) in enumerate(S):
        if total_weight + weight <= W:
            result[i] = 1
            total_weight += weight
            total_value += value
        
        else:
            fraction = (W - total_weight)/ weight
            result[i] = fraction
            total_value += value * fraction
            break
    
    return total_value, result

items = [(10, 60), (20, 100), (30, 120)]  # Example items
max_weight = 50  # Maximum weight the knapsack can hold


fractional_knapsack_value, item_fractions = fractionalKnapsack(items, max_weight)
print("Maximum value in knapsack =", fractional_knapsack_value)
print("Fractions of items taken:", item_fractions)