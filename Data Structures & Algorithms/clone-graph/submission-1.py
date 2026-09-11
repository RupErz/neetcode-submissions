"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {} # org: clone node

        if not node:
            return None

        def dfs(cur):
            if cur in clone:
                return clone[cur]
            
            cloneNode = Node(cur.val)
            clone[cur] = cloneNode
            for nei in cur.neighbors:
                cloneNode.neighbors.append(dfs(nei))
            
            return cloneNode

        return dfs(node)