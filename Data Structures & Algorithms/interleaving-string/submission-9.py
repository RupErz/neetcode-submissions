class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 2 pointer here 

        # but what if both s1 and s2 somehow at the same letter then which one do we proceed ? It will affect the substring #
        # => We gotta try both = DFS
        if len(s1) + len(s2) != len(s3):
            return False

        visited = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            
            if (i, j) in visited:
                return visited[(i, j)]

            result = False
            if i < len(s1) and s1[i] == s3[i + j]:
                result = dfs(i + 1, j)
            
            # If result is still false then we check other string
            if not result and j < len(s2) and s2[j] == s3[i + j]:
                result = dfs(i, j + 1)
            
            visited[(i, j)] = result
            return result
        
        return dfs(0, 0)