class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j):
            if (i not in range(len(word1))
                and j not in range(len(word2))):
                return 0 
            
            if i not in range(len(word1)):
                # Insert
                return 1 + dfs(i, j + 1)
            if j not in range(len(word2)):
                # Delete
                return 1 + dfs(i + 1, j)

            result = 0
            if word1[i] == word2[j]:
                result = dfs(i + 1, j + 1)
            else :
                result = min(1 + dfs(i, j + 1),
                            1 + dfs(i + 1, j),
                            1 + dfs(i + 1, j + 1))
            return result
        return dfs(0, 0)
        # match : i + 1, j + 1
        # unmatch :
        # + Insert : 1 + (i, j + 1)
        # + Delete : 1 + (i + 1, j)
        # + Replace : 1 + (i + 1, j + 1)
        # Base case : 
        # Both i, j out of bounds -> 0 operation
        # i or j out of bounds : insert / delete n remaining char
