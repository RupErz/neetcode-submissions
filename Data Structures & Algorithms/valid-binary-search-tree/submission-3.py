# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur, minNode, maxNode):
            if not cur:
                return True

            if cur.val <= minNode or cur.val >= maxNode:
                return False
            
            return dfs(cur.left, minNode, cur.val) and dfs(cur.right, cur.val, maxNode)
        
        return dfs(root, float("-inf"), float("inf"))


            
