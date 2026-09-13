class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        # Each node is a parent of itself
        # Merge: the lower with the bigger one + update its size
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        visited = set()
        def dfs(cur):
            if cur in visited:
                return
            
            visited.add(cur)
            for nei in adj[cur]:
                dfs(nei)


        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1
        
        return result

