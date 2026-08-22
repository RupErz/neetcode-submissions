class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [ i for i in range(len(word2) + 1)]

        for i in range(1, len(word1) + 1):
            newDp = [ i for i in range(len(word2) + 1)]
            newDp[0] = i
            for j in range(1, len(word2) + 1):
                if word2[j - 1] == word1[i - 1]:
                    newDp[j] = dp[j - 1]
                else:
                    newDp[j] = 1 + min(
                        dp[j - 1],
                        dp[j],
                        newDp[j - 1]
                    )
            dp = newDp
        return dp[len(word2)]