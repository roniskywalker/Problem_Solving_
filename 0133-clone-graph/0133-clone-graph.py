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
        ntoc = {None: None}
        def dfs(n):
            if n in ntoc:
                return ntoc[n]
            c = Node(n.val)
            ntoc[n] = c
            for nb in n.neighbors:
                c.neighbors.append(dfs(nb))
            return c
        return dfs(node)