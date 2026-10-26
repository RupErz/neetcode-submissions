class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = [ord(n) - ord('0') for n in num1]
        n2 = [ord(n) - ord('0') for n in num2]
        result = [0] * (len(n1) + len(n2))

        for i in range(len(n1) - 1, -1, -1):
            for j in range(len(n2) - 1, -1, -1):
                result[i + j + 1] += (n1[i] * n2[j])
        
        # Handle Carries
        for i in range(len(result) - 1, 0, -1):
            keep = result[i] % 10
            carry = result[i] // 10
            result[i] = keep
            result[i - 1] += carry
        
        result = ''.join(map(str, result)).lstrip('0') or '0'
        return result
            