class MedianFinder:

    def __init__(self):
        self.left = [] #max heap
        self.right = [] #min heap
        self.leftSize = 0
        self.rightSize = 0

    def addNum(self, num: int) -> None:
        # Left first if both empty
        if self.leftSize == 0 and self.rightSize == 0:
            heapq.heappush(self.left, -num)
            self.leftSize += 1
            return
        
        # Left side if <= to its max:
        if num <= -(self.left[0]):
            heapq.heappush(self.left, -num)
            self.leftSize += 1
        else:
            heapq.heappush(self.right, num)
            self.rightSize += 1

        # Check for rebalance
        # 2 Heaps cannot diff more than 2 (violate median rules)
        if abs(self.leftSize - self.rightSize) == 2:
            # Rebalance it so diff is at most 1
            if self.leftSize > self.rightSize:
                redundant = -heapq.heappop(self.left)
                self.leftSize -= 1
                heapq.heappush(self.right, redundant)
                self.rightSize += 1
            else:
                redundant = heapq.heappop(self.right)
                self.rightSize -= 1
                heapq.heappush(self.left, -redundant)
                self.leftSize += 1

    def findMedian(self) -> float:
        if self.leftSize == self.rightSize:
            return (-self.left[0] + self.right[0]) / 2
        else:
            if self.leftSize > self.rightSize:
                return (-self.left[0])
            else:
                return self.right[0]
