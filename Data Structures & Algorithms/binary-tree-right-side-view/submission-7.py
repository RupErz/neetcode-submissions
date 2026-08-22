# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Time : O(N) , Space: O(N)
        # q = collections.deque([root])
        # res = []

        # while q :
        #     qLen = len(q)
        #     rightNode = None # We use this to track the last node of each loop

        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node :
        #             rightNode = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if rightNode :
        #         res.append(rightNode.val)
        # return res

        # DFS: Much more simple, as long as you understand problem : 
        # Binary Tree Level Order Traversal DFS.
        # Time : O(N), Space: O(N)
        res = []

        def dfs(root, depth):
            if not root :
                return None
            
            if len(res) == depth : # This is the first time we visit the level
                res.append(root.val)

            #Prioritize right side
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        dfs(root, 0)
        return res

