class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return i
            else:
                hashSet.add(i)
                