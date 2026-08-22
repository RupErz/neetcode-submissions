class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 :
            return [[]]

        res = []

        # First we need to keep recurse until basecase 
        perms = self.permute(nums[1:]) # omit the first value each time

        for p in perms :
            for i in range(len(p) + 1): # because we need to access to the back
                copy = p.copy()
                copy.insert(i, nums[0])
                res.append(copy)
        return res
        