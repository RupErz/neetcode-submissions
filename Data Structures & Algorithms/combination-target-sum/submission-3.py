class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # 2 5 6 9
        # pick 2 OR skip 2
        # pick 2 => still can pick 2 in the future
        # skip 2 => never pick 2 in the future

        # sum = target => return
        # > target: stop 

        result = []
        def dfs(i, cur, curSum):
            if i >= len(nums) or curSum > target:
                return
            
            if curSum == target:
                result.append(cur.copy()) # avoid mutation
                return 

            # Pick 2
            cur.append(nums[i])
            dfs(i, cur, curSum + nums[i])

            cur.pop()
            # Not picking 2
            dfs(i + 1, cur, curSum)

        dfs(0, [], 0)
        return result 