# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMinValue(ptr):
            while ptr and ptr.left:
                ptr = ptr.left
            return ptr
        def delete(cur, key):
            if not cur:
                return None
            if key > cur.val:
                cur.right = delete(cur.right, key)
            elif key < cur.val:
                cur.left = delete(cur.left, key)
            else:
                if not cur.left:
                    return cur.right
                elif not cur.right:
                    return cur.left
                else:
                    minNode = findMinValue(cur.right)
                    cur.val = minNode.val
                    cur.right = delete(cur.right, minNode.val)
            return cur
        return delete(root, key)
        