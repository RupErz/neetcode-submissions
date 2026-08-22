class Solution:
    def countSubstrings(self, s: str) -> int:
        # We applied like "Longest Palindrom Substring"
        # Pick at 1 spot then widen it to 2 side L and R 
        res = 0

        # When loop, we need to treat 2 cases: odd and even length
        for i in range(len(s)):
            # odd 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r] :
                res += 1
                l, r = l - 1, r + 1
            # even 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r] :
                res += 1
                l, r = l - 1, r + 1
        return res