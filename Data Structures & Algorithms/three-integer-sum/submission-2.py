class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 sum using hashmap with target - x to find 

        # Brute force: Using 3 ptrs i, j ,k not rly bad 
        # for i / for j / for k 
        if len(nums) < 3:
            return []

        nums.sort()
        result = [] 

        for i, val in enumerate(nums):
            if val > 0:
                break

            # Avoid duplicate
            if i > 0 and val == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result