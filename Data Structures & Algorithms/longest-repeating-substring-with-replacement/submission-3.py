class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        result = 0
        count = {}
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r-l+ 1)
        return result

        