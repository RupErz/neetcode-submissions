class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u].append(v)
        
        topSort = []
        visited = set()
        visiting = set()

        # DFS Postorder : LRP
        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False
            
            visiting.add(src)

            for nei in adj[src]:
                if not dfs(nei):
                    return False
            
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
            return True
            
            topSort.append(src)
            path.pop()

        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort


        