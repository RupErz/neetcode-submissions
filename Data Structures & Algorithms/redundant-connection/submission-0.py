class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # First make a list of parent : 
        par = [ i  for i in range(len(edges) + 1)]
        0 , 1, 2, 3, 4
        # List of rank for each node ( current size )
        rank = [1] * (len(edges) + 1)
        1, 1, 1, 1, 1
        # a function find the parent of a node
        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        # a union function allow us to merge 2 node together:
        def union(a, b):
            parA, parB = find(a), find(b)

            # detect a cycle
            if parA == parB:
                return False

            # if not we will merge them using union
            if rank[parA] > rank[parB]:
                par[parB] = parA
                rank[parA] += rank[parB]
            else:
                par[parA] = parB
                rank[parB] += rank[parA]
            return True

        res = None
        for node1, node2 in edges:
            if (not union(node1, node2)) :
                res = [node1, node2]
        return res
            