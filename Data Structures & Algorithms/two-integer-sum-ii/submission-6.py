class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        recentIdx = {}

        for i in range(len(numbers)):
            cur = numbers[i]

            if (target - cur) in recentIdx:
                return [recentIdx[target - cur] + 1, i + 1]
            else:
                recentIdx[cur] = i