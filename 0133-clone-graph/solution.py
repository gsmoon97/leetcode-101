"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}  # to keep track of all cloned nodes to ensure node is cloned only once
        def clone_node(node):  # recursively clone the node
            if node in cloned:
                return cloned[node]
            
            node_clone = Node(node.val)
            cloned[node] = node_clone
            for nb in node.neighbors:
                node_clone.neighbors.append(clone_node(nb))
            
            return node_clone
        
        return clone_node(node)
