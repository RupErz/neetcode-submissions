class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Base case : # comp = 1
        mapNode = { i : [] for i in range(n) }
        for a, b in edges:
            mapNode[a].append(b)
            mapNode[b].append(a)
        
        result = 0
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return
            visit.add(node)
            for nei in mapNode[node]:
                if nei == prev :
                    continue
                dfs(nei, node)

        for node in range(n):
            if node not in visit:
                dfs(node, -1)
                result += 1
        return result
        