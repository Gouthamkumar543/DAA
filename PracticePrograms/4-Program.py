#!/usr/bin/env python
# coding: utf-8

# In[1]:


#0/1 Knapsack problem using Back tracking
def knapsack_backtracking(weights, values, capacity, n, current_weight=0, current_value=0,idx=0):
    if current_weight > capacity:
        return 0
    if idx == n:
        return current_value
    include_value = knapsack_backtracking(weights, values, capacity, n,
    current_weight + weights[idx], current_value + values[idx], idx + 1)
    exclude_value = knapsack_backtracking(weights, values, capacity, n, current_weight, current_value, idx + 1)
    return max(include_value, exclude_value)
    
# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
n = len(weights)
print("Maximum Value in Knapsack (0-1 Knapsack):", knapsack_backtracking(weights, values, capacity, n))


# In[2]:


#8-Queens Problem (Backtracking)

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_queens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_queens(board, row + 1, n):
                return True
            board[row][col] = 0
    return False


def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()


# Example usage
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_queens(board, 0, n):
    print("Solution to the 8-Queens Problem:")
    print_solution(board, n)
else:
    print("No solution exists.")


# In[6]:


#Hamiltonian Graph Problem

def is_safe(graph, path, pos, v):
    # Check if current vertex is adjacent to the previous vertex and not yet visited
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True


def hamiltonian_util(graph, path, pos, n):
    if pos == n:
        # Check if there is an edge from the last vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        return False

    for v in range(1, n):
        if is_safe(graph, path, pos, v):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1, n):
                return True
            path[pos] = -1  # Backtrack
    return False


def hamiltonian_path(graph, n):
    path = [-1] * n
    path[0] = 0  # Starting point
    if not hamiltonian_util(graph, path, 1, n):
        return "No Hamiltonian Cycle exists"
    return path


# Example usage
graph = [
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
]

n = 6
path = hamiltonian_path(graph, n)

if isinstance(path, str):
    print(path)
else:
    print("Hamiltonian Cycle:", path)

