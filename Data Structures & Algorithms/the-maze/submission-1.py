class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # ball can move up right left down (rolling)
        # ball move between 0 spaces
        # if it hit a wall -> STOP 
        # if it move it will keep rolling until hit a wall to stop.
        # True if it can stop at the destination / False otherwise

        # BFS only good when find shortest path (doable)
        # DFS ofc is useful (much simpler to do)
            # Track only the position we stop
            # Base case: T when we get to destination F if we encounter duplication

        # [0,0,1,0,0]
        # [0,0,0,0,0]
        # [0,0,0,1,0]
        # [1,1,0,1,1]
        # [0,0,0,0,0]

        visiting = set() # Track current path
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(maze), len(maze[0])

        def dfs(r, c):
            if r == destination[0] and c == destination[1]:
                return True 

            # Avoid go further if we already at this position
            if (r, c) in visiting:
                return False 
            

            visiting.add((r, c))

            for dr, dc in directions:
                curR, curC = r, c
                # Pick 1 directions and roll over it
                # Rolling until see a wall or border.
                while curR + dr in range(ROWS) and curC + dc in range(COLS) and maze[curR + dr][curC + dc] != 1:
                    curR += dr
                    curC += dc
                
                # Start picking a new directions ~ recall dfs on this
                if dfs(curR, curC):
                    return True
                
            return False # Cannot reach the destination
        
        return dfs(start[0], start[1])

