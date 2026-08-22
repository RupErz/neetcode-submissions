class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin , curMax = 1, 1 # This is product ( a x b )
        1, 0, 100
        for i in nums :
            if i == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMin
            curMin = min(curMin * i, i, curMax * i)
            curMax = max(tmp * i, i, curMax * i)
            res = max(res, curMax)
        return res
