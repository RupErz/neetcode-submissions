class CountSquares:
    # There can be duplicate points so
    # hashmap x, set x
    # stack, queue not related
    # list? But it too general
    # Hashmap and store val as freq

    # Count function: 
    # To be a valid square diagonal: abs of x and y of 2 points equal but diff from 0 (avoid same point case)
    # Once we know that 2 points, we can conclude another 2 points using logic.
    # How to update result ?
    # => Let's say with 1 query points and a dup pointA, b pointB, c pointC
    # => There will be a total of a * b * c squares from this query points

    # Time: Add O(1), Count: O(n)
    
    def __init__(self):
        self.freq = {}
        
    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) not in self.freq:
            self.freq[(x, y)] = 0
        self.freq[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        curX, curY = point
        result = 0
        for key, val in self.freq.items():
            adjX, adjY = key

            # Check if they form a square diagonal
            # If query point is one of the existing points -> Skip
            if (abs(curX - adjX) != 0 and abs(curY - adjY) != 0
                and abs(curX - adjX) == abs(curY - adjY)):   
                # This is a valid diagonal
                # Check another diagonal 
                
                if ((curX, adjY) in self.freq and (adjX, curY) in self.freq):
                    result += self.freq[(curX, adjY)] * self.freq[(adjX, curY)] * self.freq[(adjX, adjY)]

        
        return result
