class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        picked = [False] * len(nums)
        def dfs(cur):
            if len(cur) == len(nums):
                result.append(cur.copy())
                return
            
            for i in range(len(nums)):

                if picked[i]:
                    continue
                else:
                    cur.append(nums[i])
                    picked[i] = True
                    dfs(cur)
                    cur.pop() 
                    picked[i] = False


        
        dfs([])
        return result