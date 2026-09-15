class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force try each string and perform palindrome on it 
        # 2 pointer L and R to get the slices of string 
        # then we keep redoing Palindroneeeeeee

        # Sliding window NOT working because it shrink and ruin the answer
        maximum = float("-inf")
        result = s[0]

        for i in range(len(s)):
            # Odd case
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left) + 1 > maximum:
                    maximum = right - left + 1
                    result = s[left:right + 1]
                left -= 1
                right += 1

            # Even Case
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left) + 1 > maximum:
                    maximum = right - left + 1
                    result = s[left:right + 1]
                left -= 1
                right += 1
        
        return result

