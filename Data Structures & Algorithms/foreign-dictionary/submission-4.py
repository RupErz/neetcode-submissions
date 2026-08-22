class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            preWord = words[i]
            postWord = words[i + 1]
            minLen = min(len(preWord), len(postWord))
            # If a is prefix of b => len(a) < len(b)
            # => a is lexicographically lower than b
            # Violate our sorted lexico list
            # Edge case: "z" "z" they are not prefix..
            if len(postWord) < len(preWord) and preWord[:minLen] == postWord[:minLen]:
                return ""
             
            # Compare 2 words:
            for j in range(minLen):
                if preWord[j] != postWord[j]:
                    adj[preWord[j]].add(postWord[j])
                    break
        
        visit = {} # False = visited, True = current path
        result = []

        # PostOrderDFS (Child -> Parent)
        def dfs(c):
            if c in visit:
                return visit[c]
            
            # Visited but still in current path
            visit[c] = True 

            for nei in adj[c]:
                if dfs(nei):
                    return True
            # Visited but no longer in current path
            visit[c] = False
            result.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        result.reverse()
        return "".join(result)
        
            
