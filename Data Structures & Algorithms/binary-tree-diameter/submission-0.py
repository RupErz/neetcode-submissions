# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Using global variable:
        self.res = 0
        if not root:
            return 0

        def dfs(cur):
            # left right stands for the length of edge 
            if not cur :
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res