#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Back tracking technique for Knapsack problem
def knapsack_backtracking(weights, values, capacity, n, current_weight=0, current_value=0,idx=0):
    if current_weight > capacity:
        return 0
    if idx == n:
        return current_value
    include_value = knapsack_backtracking(weights, values, capacity, n, current_weight + weights[idx], current_value + values[idx], idx + 1)
    exclude_value = knapsack_backtracking(weights, values, capacity, n, current_weight, current_value, idx + 1)
    return max(include_value, exclude_value)
    
# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
n = len(weights)
print("Maximum Value in Knapsack (Backtracking Knapsack):", knapsack_backtracking(weights, values, capacity, n))

