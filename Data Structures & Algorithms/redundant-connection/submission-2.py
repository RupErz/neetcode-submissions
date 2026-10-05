class UnionFind:
    def __init__(self, n):
        self.levels = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            tmp = self.parent[cur]
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = tmp
        return cur

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False # cycle detected

        if self.levels[p1] > self.levels[p2]:
            self.parent[p2] = p1
            self.levels[p1] += 1
        else:
            self.parent[p1] = p2
            self.levels[p2] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))

        for edge in edges:
            a, b = edge
            if not unionFind.union(a, b):
                return [a, b]
        

