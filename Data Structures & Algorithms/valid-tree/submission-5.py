class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # To know if its a tree then find out if its having a cycle
        # Build an adjacency list - Undirected graph
        # {
        #     0: [1, 2, 3]
        #     1: [0, 4]
        #     2: [0]
        #     3: [0]
        #     4: [1]
        # }
        adj = { i:[] for i in range(n) }
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set() # to detect cycle
        # Use dfs to detect cycle
        def dfs(cur, prev):
            # F when cycle or it's not connecting to any node
            if cur in visited:
                return False
            
            # Issue 1: Node 0 and 3 will revisit how do i stop that ?
            # => Avoid revisiting only the previous node
            visited.add(cur)
            for nei in adj[cur]:
                if nei == prev:
                    continue
                if not dfs(nei, cur):
                    return False

            return True
        
        if not dfs(0, -1):
            return False
        # if we not visited all means one node is not connected
        if len(visited) != n:
            return False
        return True



        # PHOI DO - COMPLETED
        # {
        #     0: 1, 2
        #     1: 0, 2
        #     2: 0, 1
        # }

        





        # And also a node can be a lone wolf too
        # Either lone worlf or cycle = No Tree