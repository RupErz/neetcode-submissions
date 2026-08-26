class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0

        while l < r:
            canHold = min(heights[l], heights[r]) * (r - l)
            maximum = max(maximum, canHold)

            # Start moving: Move the smaller one to find a better volume
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        
        return maximum