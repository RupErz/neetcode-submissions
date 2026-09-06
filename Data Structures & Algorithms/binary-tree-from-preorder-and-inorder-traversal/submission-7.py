# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, val in enumerate(inorder):
            indices[val] = i
        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return None
                
            # Find the current root
            rootVal = preorder[self.preIdx]
            mid = indices[rootVal]
            self.preIdx += 1 # Move to next root

            root = TreeNode(rootVal)

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(preorder) - 1)
