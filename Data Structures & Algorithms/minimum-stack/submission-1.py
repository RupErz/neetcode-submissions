class MinStack:

    def __init__(self):
        self.stack = []
        self.minSoFar = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minSoFar.append(val)
        else:
            if self.minSoFar[-1] > val:
                self.minSoFar.append(val)
            else:
                self.minSoFar.append(self.minSoFar[-1])
            self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minSoFar.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minSoFar[-1]
        
