class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.quickSort(0, len(self.nums) - 1)
        return self.nums[len(self.nums) - self.k]

    def quickSort(self, left, right):
        if ( left < right ): # At least 2 element
            j = self.partition(left, right) 
            self.quickSort(left, j - 1)
            self.quickSort(j + 1, right)
    def partition(self, l, r):
        pivot = self.nums[l]
        i, j = l + 1, r
        while True :
            while i <= j and self.nums[i] <= pivot :
                i += 1
            while i <= j and self.nums[j] > pivot :
                j -= 1
            if i >= j :
                break
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
    # Swap pivot with nums[j]
        self.nums[l], self.nums[j] = self.nums[j], self.nums[l]
        return j