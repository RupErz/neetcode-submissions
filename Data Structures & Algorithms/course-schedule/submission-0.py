class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each of course 
        mapCourse = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            mapCourse[crs].append(pre)
        visit = set()

        def dfs(node):
            if node in visit :
                return False
            if mapCourse[node] == []:
                return True

            visit.add(node)
            for preq in mapCourse[node]:
                if not dfs(preq): return False
            visit.remove(node)
            mapCourse[node] = [] # Mark this node as possible
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True