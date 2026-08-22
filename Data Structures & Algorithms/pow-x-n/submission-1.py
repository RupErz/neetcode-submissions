class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x, n):
            if n == 0:
                return 1

            if x == 0 :
                return 0
            
            result = x
            result *= recursion(x, n - 1)

            return result

        result = recursion(x, abs(n) // 2)
        square = result * result
        
        if n % 2 == 1:
            square = square * x

        if n < 0:
            return 1 / square
        return square
            
        

        # Org approach : O(N)
        # Optimization : O(logN)