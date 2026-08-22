"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # This is deep copy , every copy we made have to be deep copy
        # the node itself and within the neighbors list.
        # oldToNew = {}
        # def dfs(node):
        #     if node in oldToNew:
        #         # Return the copy
        #         return oldToNew[node]
        #     # Create a deep copy 
        #     copy = Node(node.val)
        #     oldToNew[node] = copy
        #     for nei in node.neighbors :
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        # return dfs(node) if node else None

        # BFS : 
        # Hash map to store clone of each node
        if not node :
            return None
        oldToNew = {} 
        # initialize a deque with a node as first value
        q = collections.deque([node])
        copy = Node(node.val)
        oldToNew[node] = copy
        while q :
            curNode = q.popleft()

            for nei in curNode.neighbors:
                if nei not in oldToNew :
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[curNode].neighbors.append(oldToNew[nei])
        return oldToNew[node] 
        # Time : Loop each node exactly 1 time : N
        # Each node visited we reach each edge exactly 1 (neighbors)
        # Time Complexity : O(N + V)
        # Why ? While: iterate 1 per node
        # For loop : Iterate 1 for each edge (we have hashmap to avoid dup)
                

