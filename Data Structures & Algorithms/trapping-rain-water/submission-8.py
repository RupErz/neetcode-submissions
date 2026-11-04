class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        result = 0

        while l < r:
            if maxL < maxR:
                # Move left
                l += 1
                if height[l] > maxL:
                    maxL = height[l]
                else:
                    result += min(maxL, maxR) - height[l]

            else:
                # Move right
                r -= 1
                if height[r] > maxR:
                    maxR = height[r]
                else:
                    result += min(maxL, maxR) - height[r]

        return result
                




