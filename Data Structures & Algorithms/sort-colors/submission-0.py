class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Count the number of the number freq
        freq = Counter(nums)
        order = deque() # Using deque to track the order of number pop
        for i in [0, 1, 2]:
            if freq[i] > 0:
                order.appendleft((i, freq[i])) # 0 first, then 1 and 2
        
        idx = 0
        while order:
            target, amt = order.pop()

            if nums[idx] != target:
                nums[idx] = target
            
            if amt - 1 != 0:
                order.append((target, amt - 1))

            idx += 1
        
            