class RandomizedSet:

    def __init__(self):
        # Hashmap or Set with O(1) for insert and remove operations.
        self.numMap = {} # Used for O(1) check if a in b
        self.numList = [] # Used to access with index
        self.index = 0 # Track current index in the array

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        
        self.numMap[val] = self.index
        self.numList.append(val)
        self.index += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        
        curIndex = self.numMap[val]

        # Delete from the numList with O(1)

        # Swap deleted spot with last spot
        deletedVal = self.numList[curIndex] 
        lastVal = self.numList[-1]
        self.numList[curIndex], self.numList[-1] = lastVal, deletedVal

        # Update our hashmap and list after swap
        self.numMap[lastVal] = curIndex
        self.numList.pop() # Took O(1)
        del self.numMap[val]


        self.index -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()