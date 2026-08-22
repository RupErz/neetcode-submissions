class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create n tree comp with each node is a parent of itself
        par = [ i for i in range(n)]

        # To store the size of each components, ini = 1
        rank = [1] * n

        # A function to find the parent of a current node
        def find(n):
            res = n
            while res != par[res]:
                # Path compression
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # Same parent = alr merged
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else :
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1 # We successfully did a union
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


        