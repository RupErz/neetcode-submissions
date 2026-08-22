# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            # Base case: if root is None, return ?
            if not node:
                return None 

            # If current node is p or q, what should we return?
            if node == p or node == q:
                return node

            # Recurse on left and right
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Now the key decision:
            # - If BOTH left and right found something, current node is LCA
            if left and right:
                return node
            # - If only left found something, what does that mean?
            elif left:
                return left
            # - If only right found something, what does that mean?
            else:
                return right
        return dfs(root)
