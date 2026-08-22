class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # This is when we finish break the words (base)

        for i in range(len(s) - 1, -1, -1) :

            # Loop through every words to check :
            for w in wordDict :
                # Check the substring from starting from index i to i + w
                if i + len(w) <= len(s) and s[i: i + len(w)] == w :
                    dp[i] = dp[i + len(w)] 
                    # e.g: neetcode, at idx 4 'code' we match and having 
                    # our word added we reach idx 8 = BASE CASE
                if dp[i]:
                    break
        return dp[0]
        # Time : O(m * n * k)
        # String slices : O(k) / Comparing string : O(k) , k is the 
        # length of the words or substring