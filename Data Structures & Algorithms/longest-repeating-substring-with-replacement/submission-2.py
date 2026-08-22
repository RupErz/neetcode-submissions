class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq = [0] * (26) #26 ascii char
        L = 0
        maxfreq = 0
        
        for R in range(len(s)):
            freq[ord(s[R]) - 65] += 1

            while (R - L + 1) - max(freq) > k:
                freq[ord(s[L]) - 65] -= 1
                L += 1
            
            result = max(result, R - L + 1)
        return result






            
        