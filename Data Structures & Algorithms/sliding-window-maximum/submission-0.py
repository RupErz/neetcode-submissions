class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        if size < k : 
            return []
        elif size == k :
            return [max(nums)]
        else : 
            l = 0
            res = []
            for r in range(k - 1, size):
                res.append(max(nums[l:r + 1]))
                l += 1
            return res