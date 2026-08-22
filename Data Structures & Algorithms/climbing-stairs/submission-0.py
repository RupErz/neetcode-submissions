class Solution:
    def climbStairs(self, n: int) -> int:
        def backtrack(cur):
            if cur > n :
                return 0
            if cur == n :
                return 1
             
            res = (backtrack(cur + 1) +
                backtrack(cur + 2))
            return res
        result = backtrack(0)
        return result