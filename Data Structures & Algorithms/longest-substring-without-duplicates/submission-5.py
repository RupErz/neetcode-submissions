class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = set()
        result = 0
        L = 0
        for R in range(len(s)):
            if s[R] in arr:
                while s[R] in arr:
                    arr.remove(s[L])
                    L += 1
            arr.add(s[R])
            result = max(result, R - L + 1)
        return result
