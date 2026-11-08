class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(i, total, arr):
            if total == target:
                result.append(arr.copy())
                return 
            
            if total > target or i >= len(candidates):
                return
            
            # Pick 
            arr.append(candidates[i])
            dfs(i + 1, total + candidates[i], arr)

            # Not pickj
            arr.pop()
            cur = i
            while cur + 1 < len(candidates) and candidates[cur + 1] == candidates[cur]:
                cur += 1
            dfs(cur + 1, total, arr)
        

        dfs(0, 0, [])
        return result
