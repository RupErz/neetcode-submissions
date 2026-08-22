class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target = -1
        # Finding the spot before the decreasing pattern
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                target = i
                break

        # If target still -1 meaning that it completely reversal:
        if target == -1:
            nums.reverse()
            return 
        # Find the upcoming number in decreasing pattern (smallest)
        # nums[i:] find the smallest within this BUT have to > cur i
        replace = len(nums) - 1
        for i in range(len(nums) - 1, target, -1):
            if nums[i] > nums[target]:
                replace = i
                break
        # Replace target and replace
        temp = nums[target]
        nums[target] = nums[replace]
        nums[replace] = temp

        # Reverse the entire string after the target
        nums[target + 1:] = nums[target + 1:][::-1]


        # 3 2 1 => if idx = 0 => return the reversal of the string
        