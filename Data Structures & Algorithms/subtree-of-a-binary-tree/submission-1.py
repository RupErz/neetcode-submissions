# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Deciding the base case :
        if not subRoot and root :
            return True # an empty tree always a subtree
        if not root and subRoot:
            return False

        if self.sameTree(root, subRoot):
            return True
        # If one of subtree is True that means always True since we 
        # have subtree.
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
        

    def sameTree(self, s, t):
        if not s and not t :
            return True
        
        if s and t and s.val == t.val :
            return(
                self.sameTree(s.left, t.left)
                and self.sameTree(s.right, t.right))
        # reach this means one of them is Null
        return False

    

