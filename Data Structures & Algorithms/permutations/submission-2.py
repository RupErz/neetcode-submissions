class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in nums : #Loop through each number
                if i not in cur :
                    cur.append(i)
                    dfs()
                    cur.pop()
        dfs()
        return res
