# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # res = []
        # def dfs(root, maxVal):
        #     if not root :
        #         return None

        #     if root.val >= maxVal :
        #         res.append(root)
        #         maxVal = root.val
        #     dfs(root.left, maxVal)
        #     dfs(root.right, maxVal)
        # dfs(root, root.val)
        # return len(res)

        def dfs(root, maxVal):
            if not root :
                return 0

            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)

            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            return res
        return dfs(root, root.val)