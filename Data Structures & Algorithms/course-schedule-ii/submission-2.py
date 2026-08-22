class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i:[] for i in range(numCourses)}

        for src, dst in prerequisites:
            adj[src].append(dst)

        visit = set()
        cycle = set()
        result = []

        def dfs(i): # i is the current course we at !
            if i in cycle: # We already visit this = cycle detect
                return False
            
            # Avoid recompute a course we already process !
            if i in visit: # We already success process this course !
                return True

            # Start adding into our current cycle recursion
            cycle.add(i)

            # Visit its preq list:
            for preq in adj[i]:
                if not dfs(preq): # If it end up cycle 
                    return False
            
            cycle.remove(i) # We done traverse this course
            visit.add(i)
            result.append(i)

            return True
        
        # Visit each course
        for i in range(numCourses):
            if not dfs(i): # As long as there is a cycle = False
                return []
        return result

