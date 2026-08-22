class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 0
        max_len = 1
        maxL, maxR = 0, 0
        for i in range(len(s)):
            # Odd
            l, r = i, i
            while ((l - 1) in range(len(s)) and (r + 1) in range(len(s))
                and s[l - 1] == s[r + 1]):
                l -= 1
                r += 1
            odd = (r - l) + 1
            if max_len < odd:
                max_len = odd
                maxL = l
                maxR = r
            
            # Even
            l = i
            r = i + 1
            if r in range(len(s)) and s[l] == s[r]:
                while ((l - 1) in range(len(s)) and (r + 1) in range(len(s))
                    and s[l - 1] == s[r + 1]):    
                    l -= 1
                    r += 1
                even = (r - l) + 1
                if max_len < even:
                    max_len = even
                    maxL = l
                    maxR = r
        return s[maxL : maxR + 1]    

