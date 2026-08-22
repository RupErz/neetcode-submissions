class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP: Bottom - up ( Cal the subproblem - base case )
        # We know that starting at 3, LIS length is only 1 (base case)
        cache = { len(nums) - 1 : 1}

        for i in range(len(nums) - 2, -1, -1):
            LIS = 1
            # We have to loop through the rest to check whether it ASC
            for n in range(i + 1, len(nums), 1):
                if nums[i] < nums[n] :
                    LIS = max(LIS, 1 + cache[n])
            cache[i] = LIS
        return max(cache.values())


            