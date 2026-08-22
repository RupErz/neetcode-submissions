# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS : O(N) Space: O(N) ,res var store all node it traverse
        # q = deque([root])
        # res = []
        # while q :
        #     new = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             new.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if new :
        #         res.append(new)
        # return res

        #DFS : Time: O(N) Space: O(N)
        res = []

        def dfs(root, depth):
            if not root :
                return None
            if len(res) == depth :
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)


        dfs(root, 0)
        return res

