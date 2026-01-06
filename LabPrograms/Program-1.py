#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


#Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]       # element to be inserted
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # shift element right
            j -= 1
        arr[j + 1] = key   # insert key in correct position
    return arr

# Example usage
data = [12, 11, 13, 5, 6]
print(insertion_sort(data))  # Output: [5, 6, 11, 12, 13]


# In[3]:


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


# In[4]:


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


# In[5]:


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

