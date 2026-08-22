class Solution:
    # [1, 3]
    # => [1, 4]
    # => [1: index 0, 2, 3, 4: index 1] <= pivot means belong to that index

    # Before ; Looping over an entire list
    # Optimize with Binary Search
    # [1, 2, 5, 9] random = 3 how to find where it belong to with BS
    def __init__(self, w: List[int]):
        self.culSum = []

        curSum = 0
        for i in range(len(w)):
            curW = w[i]
            curSum += curW
            self.culSum.append(curSum)


    def pickIndex(self) -> int:
        rand = random.randint(1, self.culSum[-1])

        # Perform a binary search instead of looping entire array
        l, r = 0, len(self.culSum) - 1
        while l < r:
            mid = (l + r) // 2

            if rand > self.culSum[mid]:
                l = mid + 1
            else:
                r = mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()