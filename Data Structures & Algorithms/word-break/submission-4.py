class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Trie ? But there can be many paths ?
        # Let say neetcode, nee can be a words, so a new path open we gotta explore it => DFS traversal
        visited = {}
        def dfs(i):
            if i == len(s):
                return True
            
            if i in visited:
                return visited[i]

            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i + len(w)):
                        visited[i] = True
                        return True
            
            visited[i] = False
            return False
        
        return dfs(0)


        


