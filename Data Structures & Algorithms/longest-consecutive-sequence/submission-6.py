class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSets = set()
        for n in nums:
            numSets.add(n)

        # Starting number = no N - 1 exist in numsets
        # Only sequencing if 1. start num 2. Exist n + 1
        longest = 0

        for n in nums:     
            curLength = 1
            curNum = n
            if curNum - 1 not in numSets:
                while curNum + 1 in numSets:
                    curLength += 1
                    curNum += 1
            longest = max(longest, curLength)
        
        return longest 

            
            




