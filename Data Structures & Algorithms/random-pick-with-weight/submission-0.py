class Solution:

    def __init__(self, w: List[int]):
        self.culSum = []

        curSum = 0
        for i in range(len(w)):
            curW = w[i]
            curSum += curW
            self.culSum.append(curSum)


    def pickIndex(self) -> int:
        rand = random.randint(1, self.culSum[-1])

        for i in range(len(self.culSum)):
            if rand <= self.culSum[i]:
                return i



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()