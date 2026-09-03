# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return False

            if root.val == subRoot.val and self.isSameBranch(root, subRoot):
                return True
            # How to make it still consider another case if there are multiple subRoot head values in the branch 
            return dfs(root.left) or dfs(root.right)
        return dfs(root)


    def isSameBranch(self, root, subroot):
        if not root and not subroot:
            return True

        if not root or not subroot:
            return False

        if root.val != subroot.val:
            return False

        return self.isSameBranch(root.left, subroot.left) and self.isSameBranch(root.right, subroot.right)
        