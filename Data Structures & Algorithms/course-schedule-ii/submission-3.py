class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for tar, preq in prerequisites:
            adj[tar].append(preq)

        visited = {}
        result = []
        def dfs(i):
            if i in visited:
                return visited[i] == False
            
            visited[i] = True # Start progressing
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            result.append(i)
            visited[i] = False # Done with processed
            
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        
        return result

        # 0: 
        # 1: 0
        # 2: 
