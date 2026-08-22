# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursive DFS with global variable
        # if not root :
        #     return True
        # self.res = True

        # def dfs(cur):
        #     if not cur :
        #         return 0

        #     left = dfs(cur.left)
        #     right = dfs(cur.right)

        #     if left - right not in range(-1, 2):
        #         self.res = False

        #     return 1 + max(left, right)
        # dfs(root)
        # return self.res

        # Recursive DFS

        def dfs(root):
            # this function return a pair of value : boolean + height of tree
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balance, 1 + max(left[1], right[1])]

                #Imagine if 1 node is not balanced , it lead to another unblanc
                # Meaning that we ensure the result is False
        res = dfs(root)
        return res[0]
