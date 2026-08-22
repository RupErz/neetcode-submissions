class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x, n):
            if n == 0:
                return 1
            
            half = recursion(x, n // 2)
            half = half * half

            # Times with x everytime our n is odd
            if n % 2 == 1:
                half *= x
            return half

        result = recursion(x, abs(n))
        if n < 0 :
            result = 1 / result
        return result

        # Org approach : O(N)
        # Optimization : O(logN)