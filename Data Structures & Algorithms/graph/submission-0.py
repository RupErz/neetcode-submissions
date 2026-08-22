class GraphNode:
    def __init__(self, value = -1):
        self.value = value
        self.neighbor = {}

class Graph:
    
    def __init__(self):
        self.root = GraphNode()

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.root.neighbor:
            self.root.neighbor[src] = set()
        if dst not in self.root.neighbor:
            self.root.neighbor[dst] = set()
        self.root.neighbor[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.root.neighbor:
            return False
        if dst in self.root.neighbor[src]:
            self.root.neighbor[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if dst in self.root.neighbor[src]:
            return True

        visited = set()
        def dfs(curSrc):
            if curSrc == dst:
                return True
            if curSrc in visited:
                return False

            visited.add(curSrc)
            for nei in self.root.neighbor[curSrc]:
                if dfs(nei):
                    return True                 
            return False

        return dfs(src)

        
                
