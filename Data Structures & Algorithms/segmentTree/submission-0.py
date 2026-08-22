class Node:
    def __init__(self, total, L, R):
        self.total = total
        self.left = None
        self.right = None
        self.leftIdx = L
        self.rightIdx = R

class SegmentTree:
    # Should be better by: total, leftIdx, rightIdx
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    # O(N)
    def build(self, nums, l, r):
        if l == r:
            return Node(nums[l], l, r)
        M = (l + r) // 2
        root = Node(0, l, r)
        root.left = self.build(nums, l, M)
        root.right = self.build(nums, M + 1, r)
        root.total = root.left.total + root.right.total
        return root
    
    # O(logN)
    def update(self, index: int, val: int) -> None:
        current = self.root
        def recursion(cur, index, val):
            if cur.leftIdx == cur.rightIdx:
                cur.total = val
                return
            M = (cur.leftIdx + cur.rightIdx) // 2
            if index > M:
                recursion(cur.right, index, val)
            else:
                recursion(cur.left, index, val)
            cur.total = cur.left.total + cur.right.total 
        recursion(current, index, val)

    def query(self, L: int, R: int) -> int:
        current = self.root
        def recursion(cur, L, R):
            if cur.leftIdx == L and cur.rightIdx == R:
                return cur.total
            M = (cur.leftIdx + cur.rightIdx) // 2
            if L > M:
                # Go to right side
                return recursion(cur.right, L, R)
            elif R <= M:
                return recursion(cur.left, L, R)
            else:
                return (recursion(cur.left, L, M)
                + recursion(cur.right, M + 1, R))
        return recursion(current, L, R)

