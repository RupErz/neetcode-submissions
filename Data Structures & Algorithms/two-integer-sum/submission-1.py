class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target :
        #             return [i, j]

        # Sol 2 : Using hash map
        hashmap = {}
        for idx, val in enumerate(nums):
            rem = target - val
            if rem in hashmap :
                return [hashmap[rem], idx]
            else:
                hashmap[val] = idx
                