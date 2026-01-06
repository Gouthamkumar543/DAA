#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Greedy Construction of minimal spanning tree using
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


# In[3]:


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

