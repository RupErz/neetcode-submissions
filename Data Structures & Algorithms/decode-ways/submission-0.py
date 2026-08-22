class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 } # Act like base case and empty case

        def dfs(i) :
            if i in dp : # If we ever reach base case or it's empty
                return dp[i]
            if s[i] == '0':
                # We skip this char
                return 0
            res = dfs(i + 1)

            # Check for another character after ( 2 digits )
            if (i + 1) < len(s) and (s[i] == '1' or s[i] == '2' 
            and s[i + 1] in '0123456'):
                res += dfs(i + 2)
            
            #Caching them 
            dp[i] = res
            return res
        return dfs(0)


