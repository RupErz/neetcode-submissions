class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = False
        second = False
        third = False
        for i, j, k in triplets:
            if i <= target[0] and j <= target[1] and k <= target[2]:
                if i == target[0]:
                    first = True
                if j == target[1]:
                    second = True
                if k == target[2]:
                    third = True
        
        return first and second and third
