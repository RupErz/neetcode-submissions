class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = -1
        result = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxHeight:
                result.append(i)
                maxHeight = max(maxHeight, heights[i])
        return sorted(result)
