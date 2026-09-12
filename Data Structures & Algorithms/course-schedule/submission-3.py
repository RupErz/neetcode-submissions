class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # {
        #     2: 3
        #     1: 2
        #     3: 
        #     4: 2
        # }
        # make a list like this, then traverse recursively and if its empty for a class then we study and return True then mark it somewhere like {3: True}
        # The only thing i scare is one class might have 2 preq ?

        # Build the adjacency list
        courseMap = { i:[] for i in range(numCourses) }
        for cur, preq in prerequisites:
            courseMap[cur].append(preq)


        visited = set()
        def dfs(cur):
            # Cycle detected
            if cur in visited:
                return False 
            # can learn this class independently
            if len(courseMap[cur]) == 0:
                return True

            visited.add(cur)
            # Recursively visit its neighbor to verify
            for nei in courseMap[cur]:
                if not dfs(nei):
                    return False
            visited.remove(cur)

            # If we confirm this class is True then we clear its preq to avoid recomputing in the future
            courseMap[cur] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        
