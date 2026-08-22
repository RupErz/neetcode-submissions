class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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
