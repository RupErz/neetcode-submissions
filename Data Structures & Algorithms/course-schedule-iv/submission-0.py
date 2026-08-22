class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        # We rotate the pointer direction logic
        for u, v in prerequisites:
            adj[v].append(u)
        
        # A hash map store preq list for a current course (key)
        preq = {}
        def dfs(i):
            if i not in preq:
                preq[i] = set()
                for nei in adj[i]:
                    preq[i] = preq[i] | dfs(nei)
                preq[i].add(i)
            return preq[i]

        for n in range(numCourses):
            dfs(n)
        
        result = []
        for u, v in queries:
            if u in preq[v]:
                result.append(True)
            else:
                result.append(False)
        return result
        