class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        noDup = set()
        maximum = 0

        for r in range(len(s)):
            if s[r] in noDup:
                # Keep popping left until it no longer dup
                while s[r] in noDup:
                    noDup.remove(s[l])
                    l += 1
            
            noDup.add(s[r])
            
            # Cal the window
            maximum = max(maximum, r - l + 1)
        
        return maximum
