#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Greedy implementation for Knapsack problem
def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    items = []
    for i in range(n):
        items.append((values[i] / weights[i], values[i], weights[i]))
    items.sort(reverse=True, key=lambda x: x[0])
    total_value = 0
    for item in items:
        if capacity <= 0:
            break
        value_per_weight, value, weight = item
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value_per_weight * capacity
            capacity = 0
    return total_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Fractional Knapsack Maximum Value:", fractional_knapsack(weights, values, capacity))

