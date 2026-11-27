# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur):
            if not cur:
                return 0

            left = dfs(cur.left)

            if left == -1:
                return -1
            right = dfs(cur.right)

            if right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
        
        
        return dfs(root) != -1
        

