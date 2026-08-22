class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n :
            return True
        # Create a hashmap of node and its neighbors
        mapNode = { i : [] for i in range(n) }
        for node, des in edges:
            # Since they are undirected
            mapNode[node].append(des)
            mapNode[des].append(node)
        visit = set()
        def dfs(node, prev) :
            if node in visit:
                return False
            visit.add(node)
            for nei in mapNode[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        # 1 : no cycle.
        # 2 : all nodes connected.
        return (dfs(0, -1) and len(visit) == n) 
        