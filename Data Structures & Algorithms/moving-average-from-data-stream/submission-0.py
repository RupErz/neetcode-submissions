class MovingAverage:
    # Track n latest value
    # => Deque (Queue)
    def __init__(self, size: int):
        # left is pop, right is append
        self.numList = deque()
        self.physicalSize = size
        self.logicalSize = 0
        self.curSum = 0

    def next(self, val: int) -> float:
        if self.logicalSize == self.physicalSize:
            self.curSum -= self.numList.popleft()
            self.logicalSize -= 1
        
        self.numList.append(val)
        self.curSum += val
        self.logicalSize += 1
        
        return self.curSum / len(self.numList)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
