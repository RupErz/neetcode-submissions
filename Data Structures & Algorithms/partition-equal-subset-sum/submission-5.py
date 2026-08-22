class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check if it's % 2 since we need 2 subset equal sum
        # Brute Force we need to check 1 + 2 or 1 or 1 + 3 or 1 + 2 + 3
        # Built from that we have : set([0])
        # Each iteration set + (n + 0) + n (Add whatever have inside the set wit new number)
        # As long as we can find 1 target which is n // 2 => We succeed
        # Because 1 subset = target meaning the rest is = target.
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2
        sumList = set([0])
        for i in range(len(nums) - 1, -1, -1):
            value = nums[i]
            newList = set()
            for j in sumList:
                curSum = j
                if value + curSum == target:
                    return True
                newList.add(curSum)
                newList.add(value + curSum)
            sumList = newList
        return False
        # Time : O(n * target)
        # Space : O(target)