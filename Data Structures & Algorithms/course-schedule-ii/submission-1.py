class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for u, v in prerequisites:
            adj[v].append(u)
        
        courseOrder = []
        visited = set()
        visiting = set()

        def dfs(i):
            if i in visited:
                return True
            if i in visiting:
                return False
            
            visiting.add(i)

            for nei in adj[i]:
                if not dfs(nei):
                    return False
            
            visiting.remove(i)
            visited.add(i)
            courseOrder.append(i)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        courseOrder.reverse()
        return courseOrder
