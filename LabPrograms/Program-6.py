#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

