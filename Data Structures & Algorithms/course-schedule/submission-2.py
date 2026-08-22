class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for u, v in prerequisites:
            adj[v].append(u)
        
        visited = set()
        visiting = set()
        coursesTaken = []

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
            coursesTaken.append(src)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        # Time: O(V + E) : Visiting each node or edge ONCE
        
        
        
        