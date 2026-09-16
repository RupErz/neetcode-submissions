class Solution:
    def countSubstrings(self, s: str) -> int:
        # Each char is a palindrom substring
        result = len(s)

        # Same thing we extend like last time
        for i in range(len(s)):
            # odd case
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            
            # Even case
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        
        return result