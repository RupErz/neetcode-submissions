class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O ( 26: 26 char when finding max x O(N))
        # freq = {}
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     #Increment our frequency hash map
        #     freq[s[r]] = 1 + freq.get(s[r], 0)

        #     #Checking if its a valid window or not
        #     #dict.values => list of value
        #     #dict.items => list of keys
        #     while (r - l + 1) - max(freq.values()) > k :
        #         freq[s[l]] -= 1
        #         l += 1
        #     res = max(res, r - l + 1)
        # return res


        freq = {}
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            #Increment our frequency hash map
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])

            #Checking if its a valid window or not
            #dict.values => list of value
            #dict.items => list of keys
            while (r - l + 1) - maxf > k :
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res