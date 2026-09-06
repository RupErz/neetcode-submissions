# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # sequence = all nodes unique, maximum, doesnt have to start from root
        # problem in lists:
        # [2 , -4, 2, 5, -1, -4, 25, 5]
        # => Which sequence brign the max sum
        # Algo: Iterating from start, if it make bigger , we upd max and include that sequence if it make smaller then we cut and start new list on that number
        # inorder: 10 -15 -5 15 20 5
        # preorder: -15 10 20 15 -5 5

        final = float("-inf")

        def dfs(cur):
            nonlocal final

            if not cur:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            left = max(0, left)
            right = max(0, right)

            if cur.val + left + right > final:
                final = cur.val + left + right

            return cur.val + max(left, right)


        dfs(root)
        return final