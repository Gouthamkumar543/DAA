#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Travelling sales man problem
import sys
def tsp(dp, dist, visited, n, pos, visited_count):
    if visited_count == n:
        return dist[pos][0] # Return to the start point
        
    if dp[pos][visited_count] != -1:
        return dp[pos][visited_count]
    
    ans = sys.maxsize
    for city in range(n):
        if (visited & (1 << city)) == 0:
            ans = min(ans, dist[pos][city] + tsp(dp, dist, visited | (1 << city), n, city, visited_count + 1))
    dp[pos][visited_count] = ans
    return ans
            
def traveling_salesman_problem(dist):
    n = len(dist)
    dp = [[-1] * (1 << n) for _ in range(n)]
    return tsp(dp, dist, 1, n, 0, 1)
    
# Example usage
dist = [
 [0, 10, 15, 20],
 [10, 0, 35, 25],
 [15, 35, 0, 30],
 [20, 25, 30, 0]
]
print("Traveling Salesman Problem Minimum Cost:", traveling_salesman_problem(dist))


# In[3]:


#Multistage Graph problem
def multistage_graph(graph, n):
    dist = [float('inf')] * n
    dist[n-1] = 0 # The destination vertex has zero distance
    for stage in range(n-2, -1, -1):
        for next_stage in range(stage+1, n):
            if graph[stage][next_stage] != float('inf'):
                dist[stage] = min(dist[stage], graph[stage][next_stage] + dist[next_stage])
    return dist[0]
    
# Example usage
n = 4
graph = [
 [0, 10, float('inf'), float('inf')],
 [float('inf'), 0, 20, float('inf')],
 [float('inf'), float('inf'), 0, 30],
 [float('inf'), float('inf'), float('inf'), 0]
]
print("Multistage Graph Minimum Cost:", multistage_graph(graph, n))


# In[4]:


#All-Pairs Shortest Paths (Warshal)
def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
    
# Example usage
graph = [
 [0, 3, float('inf'), float('inf')],
 [3, 0, 1, 5],
 [float('inf'), 1, 0, 2],
 [float('inf'), 5, 2, 0]
]
result = floyd_warshall(graph)
print("Floyd-Warshall All-Pairs Shortest Paths:")
for row in result:
    print(row)


# In[5]:


#Single-Source Shortest Paths (Bellman ford)
def bellman_ford(graph, V, source):
    dist = [float('inf')] * V
    dist[source] = 0
    for _ in range(V-1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Check for negative weight cycle
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return None
    return dist
    
# Example usage
V = 5
graph = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
source = 0
print("Bellman-Ford Shortest Paths:", bellman_ford(graph, V, source))


# In[8]:


#Optimal Binary Search Trees
def optimal_bst(freq, n):
    cost = [[0] * n for _ in range(n)]
    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if length == 1:
                cost[i][j] = freq[i]
            else:
                cost[i][j] = float('inf')
                for r in range(i, j+1):
                    left_cost = cost[i][r-1] if r > i else 0
                    right_cost = cost[r+1][j] if r < j else 0
                    total_cost = left_cost + right_cost + sum(freq[i:j+1])
                    cost[i][j] = min(cost[i][j], total_cost)
    return cost[0][n-1]
# Example usage
freq = [10, 12, 20, 30]
n = len(freq)
print("Optimal BST Cost:", optimal_bst(freq, n))

