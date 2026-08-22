class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remain = 1
        for i in range(len(digits) - 1, -1, -1):
            curDigits = digits[i] + remain
            if curDigits == 10:
                digits[i] = 0
            else:
                digits[i] = curDigits
                remain = 0
                break
        
        if remain == 1:
            digits.insert(0, remain)

        return digits
            
