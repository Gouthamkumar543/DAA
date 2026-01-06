#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Binary Search
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
arr = [1, 5, 5, 6, 7, 21, 51, 54, 84]
target = 6
print("Binary Search:", binary_search(arr, target))


# In[3]:


#Sequential Search
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

# Example usage
data = [10, 25, 30, 45, 50]
target = 30
result = sequential_search(data, target)

if result != -1:
    print ("Target found at index: ",result)
else:
    print("target not found")

