#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Branch and bound for knapsack problem
import queue
class Knapsack:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)

    def bound(self, u, total_weight, total_value):
        if total_weight >= self.capacity:
            return 0
        upper_bound = total_value
        j = u
        total_weight_tmp = total_weight

        while j < self.n and total_weight_tmp + self.weights[j] <= self.capacity:
            total_weight_tmp += self.weights[j]
            upper_bound += self.values[j]
            j += 1

        if j < self.n:
            upper_bound += (self.capacity - total_weight_tmp) * self.values[j] / self.weights[j]

        return upper_bound

    def knapsack_branch_bound(self):
        max_value = 0
        q = queue.PriorityQueue()

        # Initial bound from root node
        initial_bound = self.bound(0, 0, 0)
        q.put((-initial_bound, 0, 0, 0))  # (priority by -bound, value, weight, level)

        while not q.empty():
            neg_bound, total_value, total_weight, u = q.get()
            bound = -neg_bound

            if bound <= max_value:
                continue

            if u == self.n:
                continue

            if total_weight + self.weights[u] <= self.capacity:
                val_incl = total_value + self.values[u]
                wt_incl = total_weight + self.weights[u]
                if val_incl > max_value:
                    max_value = val_incl
                q.put((-self.bound(u + 1, wt_incl, val_incl), val_incl, wt_incl, u + 1))

            q.put((-self.bound(u + 1, total_weight, total_value), total_value, total_weight, u + 1))

        return max_value


# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

knapsack = Knapsack(weights, values, capacity)
print("Maximum value in Knapsack using Branch and Bound:", knapsack.knapsack_branch_bound())

