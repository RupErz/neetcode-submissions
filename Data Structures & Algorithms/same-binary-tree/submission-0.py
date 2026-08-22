# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Using DFS : Time ( p+ q)

        if not p and not q : # both Null -> same tree
            return True
        if (not p or not q) or (p.val != q.val) : # of 1 them Null -> dif tree
            return False

        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
        # We need to compare 2 branches left and right thats why we use and.
        # U can write a stack call to test.