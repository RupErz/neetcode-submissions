class CountSquares:

    def __init__(self):
        self.points = {} # (x, y): count 


    def add(self, point: List[int]) -> None:
        pX, pY = point
        if (pX, pY) not in self.points:
            self.points[(pX, pY)] = 0
        self.points[(pX, pY)] += 1

    def count(self, point: List[int]) -> int:
        curX, curY = point

        result = 0
        for pair, count in self.points.items():
            pX, pY = pair
            if pX != curX and pY != curY:
                if (curX, pY) in self.points and (pX, curY) in self.points:
                    result += (self.points[(pX, pY)] * self.points[(curX, pY)] * self.points[(pX, curY)])
        
        return result 

        # YOu miss the case if it have overlap points 

        
