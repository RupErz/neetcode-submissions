class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        pX = self.find(x)
        pY = self.find(y)
        return True if pX == pY else False

    def union(self, x: int, y: int) -> bool:
        pX, pY = self.find(x), self.find(y)
        if pX == pY:
            return False

        if self.rank[pX] < self.rank[pY]:
            self.par[pX] = pY
        elif self.rank[pX] > self.rank[pY]:
            self.par[pY] = pX
        else:
            # Arbitrarily set them
            self.par[pX] = pY
            self.rank[pY] += 1
        return True

    def getNumComponents(self) -> int:
        result = 0
        for node in self.par:
            if node == self.find(node):
                result += 1
        return result
        # O(n * height current node)
            
