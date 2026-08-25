class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            while r >= 0 and not s[r].isalnum():
                r -= 1
            while l < len(s) and not s[l].isalnum():
                l += 1
            
            if r >= 0 and l < len(s) and s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        
        return True

