class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Case: it end up more number than org digits, we gotta add or expand the array
        result = [0] + digits
        carry = 1

        for i in range(len(result) - 1, -1, -1):
            if carry == 0:
                break
            if result[i] + carry == 10:
                result[i] = 0
            else:
                result[i] = result[i] + carry
                carry = 0
        
        return result if result[0] != 0 else result[1:]