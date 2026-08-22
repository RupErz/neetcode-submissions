# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS
        #Time : O(N), Space: O(N)
        # def valid(root, left, right): #left and right here is the BOUNDARY
        #     if not root :
        #         return True
        #     if not (root.val > left and root.val < right) :
        #         return False
            
        #     return (valid(root.left, left, root.val)
        #     and valid(root.right, root.val, right))
        # return valid(root, float("-inf"), float("inf"))

        # BFS
        # Time: O(N), Space: O(N)
        if not root :
            return True
        q = collections.deque()
        q.append((root, float("-inf"), float("inf")))
        while q :
            node, left, right = q.popleft()
            if node :
                if not (node.val > left and node.val < right) :
                    return False
                q.append((node.left, left, node.val))
                q.append((node.right, node.val, right))

        return True

       


            
