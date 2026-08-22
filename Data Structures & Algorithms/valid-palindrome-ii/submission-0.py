class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 2 pointers 
        # first check palindrome normally
        # if a violation happen
        # => What should i delete ?
        # => Del both with a helper function

        def helper(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                # Can delete at most 1 (either Left or Right)
                if helper(left + 1, right) or helper(left, right - 1):
                    return True
                return False
            left += 1
            right -= 1
        
        return True