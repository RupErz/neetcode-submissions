class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP Bottoms up
        # [rob1, rob2, 0, 1, .... ,  n]
        rob1, rob2 = 0, 0
        for i in nums:
            tmp = rob2
            rob2 = max(i + rob1, rob2)
            rob1 = tmp
        return rob2



