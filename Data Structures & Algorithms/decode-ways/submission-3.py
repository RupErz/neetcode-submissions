class Solution:
    def numDecodings(self, s: str) -> int:
        visited = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            
            if i in visited:
                return visited[i]

            result = 0
            # Take 1 digits (cannot be 0 betwe 1 and 9)
            if s[i] != "0":
                result += dfs(i+1)

            # Take 2 digits (betw 10 and 26)
            # Take i and i + 1 and move to i + 2
            if i + 1 < len(s) and int(s[i] + s[i + 1]) >= 10 and int(s[i] + s[i + 1]) <= 26:
                result += dfs(i + 2)

            visited[i] = result
            return result

        return dfs(0)