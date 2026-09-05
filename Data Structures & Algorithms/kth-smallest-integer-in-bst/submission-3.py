# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force: In order print to a list then pik the kth number

        # Want to abvoid using extra space 
        # Traverse in order L Parent R and stop at node kth to return
        result = -1
        start = 0
        
        def inOrder(cur):
            nonlocal result, start
            if not cur:
                return 
            
            inOrder(cur.left)
            start += 1

            if start == k:
                result = cur.val
                return 

            inOrder(cur.right)

        inOrder(root)
        return result