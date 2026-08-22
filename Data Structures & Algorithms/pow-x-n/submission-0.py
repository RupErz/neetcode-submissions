class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x, n):
            if n == 0 :
                return 1
            
            result = x
            result *= recursion(x, n - 1)

            return result
        
        if n < 0:
            return 1/(recursion(x, abs(n)))
        return recursion(x, n)