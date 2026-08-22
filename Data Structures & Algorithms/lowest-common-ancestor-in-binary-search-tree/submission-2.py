# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # # Time : O(N), Space: O(1)
        # cur = root 
        # while cur :
        #     #if p.val > cur.val and q.val > cur.val :
        #     if (min(p.val, q.val) > cur.val):
        #         cur = cur.right
        #     #elif p.val < cur.val and q.val < cur.val :
        #     elif (max(p.val, q.val) < cur.val):
        #         cur = cur.left
        #     else:
        #         return cur
        

        # # We return when there is a split in branch left and right
        # # Even if cur = to 1 of the nodes
        # # Basically just understand that , if both nodes > or < , meaning that 
        # # we can still traverse , but if something occurs, that means a LCA
        # # is found

        #We can do recursion of this problem tomorow .
        # Time : O(N) Space : O(N)
        if not root or not p or not q :
            return None

        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root