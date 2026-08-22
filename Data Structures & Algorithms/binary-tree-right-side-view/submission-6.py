# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        while q :
            qLen = len(q)
            rightNode = None # We use this to track the last node of each loop

            for i in range(qLen):
                node = q.popleft()
                if node :
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightNode :
                res.append(rightNode.val)
        return res