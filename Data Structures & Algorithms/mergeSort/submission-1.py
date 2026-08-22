# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # Base case
        if len(pairs) == 1:
            return [pairs[0]]
        if len(pairs) == 0:
            return []
        
        #Calculating mid point 
        mid = len(pairs) // 2

        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        i, j = 0, 0
        res = []

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key :
                res.append(left[i])
                i += 1
            else :
                res.append(right[j])
                j += 1
        # Adding the remaining in case 1 list already end
        res.extend(left[i:])
        res.extend(right[j:])    
        return res
        