#!/usr/bin/env python
# coding: utf-8

# In[8]:


#0-1 Knapsack Problem (Branch and Bound)

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

            # Include item u
            if total_weight + self.weights[u] <= self.capacity:
                val_incl = total_value + self.values[u]
                wt_incl = total_weight + self.weights[u]
                if val_incl > max_value:
                    max_value = val_incl
                q.put((-self.bound(u + 1, wt_incl, val_incl), val_incl, wt_incl, u + 1))

            # Exclude item u
            q.put((-self.bound(u + 1, total_weight, total_value), total_value, total_weight, u + 1))

        return max_value


# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

knapsack = Knapsack(weights, values, capacity)
print("Maximum value in Knapsack using Branch and Bound:", knapsack.knapsack_branch_bound())


# In[9]:


#Travelling salesman problem 

import math

class TSP:
    def __init__(self, dist):
        self.dist = dist
        self.n = len(dist)
        self.final_res = math.inf
        self.visited = [False] * self.n

    def bound(self, curr_path, curr_position):
        # Calculate lower bound for the path using the minimum cost edges
        total_cost = 0
        for i in range(self.n):
            if not self.visited[i]:
                min_edge = min(self.dist[curr_position][i], self.dist[i][curr_position])
                total_cost += min_edge
        return total_cost

    def tsp_branch_bound(self, curr_path, curr_position, count, curr_cost):
        # If all cities are visited
        if count == self.n:
            # Return to the starting city
            curr_cost += self.dist[curr_position][0]
            if curr_cost < self.final_res:
                self.final_res = curr_cost
            return

        # Prune the search tree using the bound
        if curr_cost + self.bound(curr_path, curr_position) < self.final_res:
            for city in range(self.n):
                if not self.visited[city]:
                    curr_path.append(city)
                    self.visited[city] = True
                    self.tsp_branch_bound(
                        curr_path,
                        city,
                        count + 1,
                        curr_cost + self.dist[curr_position][city]
                    )
                    curr_path.pop()
                    self.visited[city] = False

    def solve(self):
        curr_path = [0]
        self.visited[0] = True
        self.tsp_branch_bound(curr_path, 0, 1, 0)
        return self.final_res


# Example usage
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp_solver = TSP(dist)
print("Minimum cost of the travelling salesman using Branch and Bound:", tsp_solver.solve())


# In[ ]:




