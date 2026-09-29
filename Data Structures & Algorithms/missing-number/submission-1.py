class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # check = set()
        # for i in nums:
        #     check.add(i)
        
        # for i in range(len(nums) + 1):
        #     if i not in check:
        #         return i
        n = len(nums)

        ideal_sum = n * (n + 1) // 2
        return abs(ideal_sum) - sum(nums)