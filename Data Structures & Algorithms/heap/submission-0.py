class MinHeap:
    
    def __init__(self):
        # Our heap index start at 1 instead at 0
        self.heap = [0]

    def push(self, val: int) -> None:
        # Ensure the structure 
        # Append to the last spot
        self.heap.append(val)

        # Start percolating up :
        i = len(self.heap) - 1
        while i > 1 and val < self.heap[(i // 2)]:
            tmp = self.heap[i // 2]
            self.heap[i // 2] = self.heap[i]
            self.heap[i] = tmp
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        # Popping the min value which is first value
        # Replace first value with last val
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down 
        while 2 * i < len(self.heap):
            if ((2 * i + 1) < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[2 * i] and
                self.heap[i] > self.heap[2 * i + 1]):
                tmp = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                tmp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i
            else:
                break
        return result

    def top(self) -> int:
        # Our heap start at index 1 
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        # Since our structure start with index 1
        self.heap.extend(nums)
        
        # Find the index that have child 
        cur = (len(self.heap) - 1) // 2

        # We percolate down at each node with children
        while cur > 0:
            i = cur
            # Start traversing back - percolating down 
            while 2 * i < len(self.heap):
                if ((2 * i + 1) < len(self.heap) and
                    self.heap[2 * i + 1] < self.heap[2 * i] and
                    self.heap[i] > self.heap[2 * i + 1]):
                    tmp = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    tmp = self.heap[2 * i]
                    self.heap[2 * i] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1

        
        