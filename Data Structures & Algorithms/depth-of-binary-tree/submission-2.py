# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Deciding when to stop
        # it can be highest first but what make we stop ? There 
        # a chance it will be next branch dfs = bfs
        # BFS shud be
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        
        return depth 
