#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr
# Example usage
arr = [64, 25, 12, 22, 11]
print("Selection Sort:", selection_sort(arr))


# In[31]:


#Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1    
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
#Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort:", merge_sort(arr))


# In[32]:


#Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
#Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Quick Sort:", quick_sort(arr))


# In[33]:


#Heap Sort
import heapq
def Heap_Sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr
# Example usage
arr = [3, 2, 1, 5, 6, 4]
print("Heap Sort:", Heap_Sort(arr))


# In[35]:


#Binary Sort
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 #Element not found
# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2
print("Binary Search:", binary_search(arr, target))


# In[41]:


#Strassen's Matrix Multiplication
# Function to add two matrices
def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Function to subtract two matrices
def subtract_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Function to perform Strassen's Matrix Multiplication
def strassen(A, B):
    # Base case: 1x1 matrix multiplication
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    # Step 1: Divide matrices A and B into sub-matrices
    mid = len(A) // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Step 2: Compute the 7 products (P, Q, R, S, T, U, V)
    P = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    Q = strassen(add_matrix(A21, A22), B11)
    R = strassen(A11, subtract_matrix(B12, B22))
    S = strassen(A22, subtract_matrix(B21, B11))
    T = strassen(add_matrix(A11, A12), B22)
    U = strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
    V = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))

    # Step 3: Compute the result sub-matrices
    C11 = add_matrix(subtract_matrix(add_matrix(P, S), T), V)
    C12 = add_matrix(R, T)
    C21 = add_matrix(Q, S)
    C22 = add_matrix(subtract_matrix(add_matrix(P, R), Q), U)

    # Step 4: Combine the sub-matrices into a single matrix
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

# Function to read a matrix from the user
def read_matrix(rows, cols, matrix_name):
    matrix = []
    print(f"Enter the elements of {matrix_name} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
        matrix.append(row)
    return matrix

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    A = read_matrix(n, n, "A")
    B = read_matrix(n, n, "B")

    print("\nResult of Strassen's Matrix Multiplication:")
    result = strassen(A, B)
    for row in result:
        print(row)

