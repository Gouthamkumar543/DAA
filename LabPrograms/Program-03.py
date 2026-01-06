#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Tree Transversal algorithms
from collections import deque

# Define a Node class for the binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inorder Traversal (DFS: Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Preorder Traversal (DFS: Root → Left → Right)
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder Traversal (DFS: Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Level Order Traversal (BFS)
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder Traversal:")
    inorder(root)       # Output: 4 2 5 1 3

    print("\nPreorder Traversal:")
    preorder(root)      # Output: 1 2 4 5 3

    print("\nPostorder Traversal:")
    postorder(root)     # Output: 4 5 2 3 1

    print("\nLevel Order Traversal:")
    level_order(root)   # Output: 1 2 3 4 5

