#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Fractional Knapsack Problem
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


# In[6]:


#Job Sequencing with Deadlines
def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = len(jobs)
    result = [None] * n
    slots = [False] * n
    for i in range(n):
        job, deadline, profit = jobs[i]
        for j in range(min(n, deadline) - 1, -1, -1):
            if not slots[j]:
                result[j] = job
                slots[j] = True
                break
    return [job for job in result if job is not None]
# Example usage
jobs = [('J1', 4, 20), ('J2', 1, 100), ('J3', 1, 19), ('J4', 1, 27), ('J5', 3, 25)]
print("Job Sequencing with Deadlines:", job_sequencing(jobs))


# In[9]:


#Minimum Cost spanning trees using Kruskal’s and Prim’s Algorithms.
#Kruskal’s Algorithm

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
        
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False
        
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []
    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
    return mst
# Example usage
n = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
print("Kruskal's MST:", kruskal(n, edges))


# In[25]:


#Prim's Algorithm

import heapq

def prim(n, graph):
    mst = []
    visited = [False] * n
    min_heap = [(0, -1, 0)]  # (weight, parent, node)
    while min_heap:
        weight, parent, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:  # skip the starting node
            mst.append((parent, u, weight))
        for v, edge_weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, u, v))
    return mst
    
# Example usage
n = 4
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

print("Prim's MST:", prim(n, graph))


# In[2]:


#Dijkstra’s Algorithm

import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)] # (distance, node)
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > distances[u]:
            continue
        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    return distances
    
# Example usage
graph = {0: [(1, 10), (2, 1)],
         1: [(0, 10), (3, 2)],
         2: [(0, 1), (3, 4)],
         3: [(1, 2), (2, 4)]}
start = 0
print("Dijkstra's Shortest Paths:", dijkstra(graph, start))

