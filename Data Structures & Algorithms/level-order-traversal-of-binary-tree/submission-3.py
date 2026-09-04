# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = deque()
        final = []
        result.append(root)

        while result:
            curLevel = []
            for i in range(len(result)):
                curNode = result.pop()
                curLevel.append(curNode.val)
                if curNode.left:
                    result.appendleft(curNode.left)
                if curNode.right:
                    result.appendleft(curNode.right)
            final.append(curLevel)
        
        return final