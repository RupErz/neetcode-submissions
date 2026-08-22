class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        result = []
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            for c in count:
                if count[c] > 0:
                    perm.append(c)
                    count[c] -= 1
                    dfs()
                    perm.pop()
                    count[c] += 1
        dfs()
        return result