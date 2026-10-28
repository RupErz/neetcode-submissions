class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = pow(-2, 31), pow(2, 31) - 1
        res = 0
        xStr = str(abs(x))
        sign = -1 if x < 0 else 1

        for i in range(len(xStr) - 1, -1, -1):
            digit = int(xStr[i])

            if res > MAX // 10 or res < MIN // 10:
                return 0
            
            if res == MAX // 10 and digit > MAX % 10:
                return 0
            
            if res == MIN // 10 and digit < MIN % 10:
                return 0
            
            res = res * 10 + digit 
            
        return res * sign