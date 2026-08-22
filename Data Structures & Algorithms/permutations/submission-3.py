class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Recursion 
        def helper(i, nums):
            if i == len(nums):
                return [[]]

            result = []
            perms = helper(i + 1, nums)

            for p in perms:
                for j in range(len(p) + 1):
                    copyPerm = p.copy()
                    copyPerm.insert(j, nums[i])
                    result.append(copyPerm)

            return result

        return helper(0, nums)