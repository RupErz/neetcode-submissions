class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Brute force :
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}
        def dfs(i, j, k):
            if (i, j, k) in cache:
                return cache[(i, j, k)]

            if (k not in range(len(s3))):
                return i == len(s1) and j == len(s2)

            if i in range(len(s1)) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    cache[(i, j, k)] = True
                    return True
                
            if j in range(len(s2)) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    cache[(i, j, k)] = True
                    return True
            
            cache[(i, j, k)] = False
            return False
        return dfs(0, 0, 0)
            
            

            
