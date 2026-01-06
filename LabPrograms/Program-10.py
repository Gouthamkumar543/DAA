#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Branch and bound for travelling sales man problem
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

