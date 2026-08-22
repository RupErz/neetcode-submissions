class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, cur, total) :
        # index: current idx in nums
        # cur: current list we at : e.g: [1,2]
        # total: current total we have 

            # 1st base case: 
            if total == target : 
                res.append(cur.copy())
                return
            if index >= len(nums) or total > target :
                return 

            # Ensure no dup -> Chosen / Not Chosen 
            # Chosen .
            cur.append(nums[index])
            dfs(index, cur, total + nums[index])

            # Not chosen .
            cur.pop()
            dfs(index + 1, cur, total)
        dfs(0, [], 0)
        return res