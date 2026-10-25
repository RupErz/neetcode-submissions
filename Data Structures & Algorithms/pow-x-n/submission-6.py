class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            res = dfs(n // 2)
            res *= res
            if n % 2 != 0:
                res *= x
            return res
        
        res = dfs(abs(n))
        
        return res if n > 0 else 1 / res

            

       