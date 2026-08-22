# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []
        def dfs(root, q):
            if not root:
                return None
            # Write the tree into the list as "in-order" LPR
            dfs(root.left, q)
            q.append(root.val)
            dfs(root.right, q)
        dfs(root, q)
        return q[k - 1] 