class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight =  height[l], height[r]
        res = 0
        while l < r :
            if maxLeft <= maxRight :
                l += 1
                res += (maxLeft - height[l]) if (maxLeft - height[l]) > 0 else 0
                maxLeft = max(maxLeft, height[l])
            else :
                r -= 1
                res += (maxRight - height[r]) if (maxRight - height[r]) > 0 else 0
                maxRight = max(maxRight, height[r])
        return res
                 
