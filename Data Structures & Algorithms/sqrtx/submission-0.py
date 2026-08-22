class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0 , x 
        result = -1
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square <= x:
                result = max(result, mid)
                l = mid + 1
            else:
                r = mid - 1
        return result