# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Using DFS : Time ( N)

        # if not p and not q : # both Null -> same tree
        #     return True
        # if (not p or not q) or (p.val != q.val) : # of 1 them Null -> dif tree
        #     return False

        # return (
        #     self.isSameTree(p.left, q.left) and
        #     self.isSameTree(p.right, q.right)
        # )
        # We need to compare 2 branches left and right thats why we use and.
        # U can write a stack call to test.

        #BFS (Stil work)
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            nodeP = q1.popleft()
            nodeQ = q2.popleft()

            if not nodeP and not nodeQ :
                continue #go to the next loop / next node
            if (not nodeP or not nodeQ) or (nodeP.val != nodeQ.val): 
                return False

            q1.append(nodeP.left)
            q1.append(nodeP.right)
            q2.append(nodeQ.left)
            q2.append(nodeQ.right)
        return True


