class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [] * (capacity)
        self.logicalSize = capacity
        self.physicalSize = 0


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() ==  self.getCapacity() :
            self.resize()
        self.array.append(n)
        self.physicalSize += 1

    def popback(self) -> int:
        self.physicalSize -= 1
        result = self.array.pop()
        return result
        

    def resize(self) -> None:
        self.logicalSize *= 2

    def getSize(self) -> int:
        return self.physicalSize
    
    def getCapacity(self) -> int:
        return self.logicalSize
