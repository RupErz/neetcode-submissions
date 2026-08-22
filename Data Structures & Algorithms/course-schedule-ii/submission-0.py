class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapCourse = { i : [] for i in range(numCourses) }
        # Map each preq with its relative course
        for course, preq in prerequisites :
            mapCourse[course].append(preq)
        output = []
        visit, cycle = set(), set()

        # visit: tracking which course have been added to output
        # cycle: tracking the cycle existence in list course.
        def dfs(i):
            if i in cycle: # There is a cycle
                return False
            if i in visit: # We alr added this
                return True
            cycle.add(i)
            for neig in mapCourse[i]:
                if not dfs(neig): return False
            cycle.remove(i) # Ensure no wrong cycle appear
            visit.add(i)
            output.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

        #Time : O(Edges + Vertices(Nodes))