# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(root, res):
        #     if not root :
        #         return None 
        #     res.append(root.val)
        #     if root.right:
        #         dfs(root.right, res)
        #     else:
        #         dfs(root.left, res)
        # dfs(root, res)
        # return res

        #Try using BFS :
        q = deque([root])
        res = []
        while q and root: 
            qLength = len(q)
            for i in range(qLength):
                node = q.popleft()

                if i == qLength - 1 :
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
                

        
