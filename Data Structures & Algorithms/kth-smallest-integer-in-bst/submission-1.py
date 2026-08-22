# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time : O(N), Space: O(N)
        # q = []
        # def dfs(root, q):
        #     if not root:
        #         return None
        #     # Write the tree into the list as "in-order" LPR
        #     dfs(root.left, q)
        #     q.append(root.val)
        #     dfs(root.right, q)
        # dfs(root, q)
        # return q[k - 1] 

        # Iterative DFS : In Order 
        # If cur reach Null -> we pop the stack -> We visit the node
        stack = []
        n = 0 # Number of node we visited
        cur = root
        while cur or stack :
            while cur :
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            n += 1
            if n == k :
                return node.val
            cur = node.right