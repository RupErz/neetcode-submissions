class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()

        for num in nums:
            if num in freq:
                return True
            freq.add(num)
        
        return False