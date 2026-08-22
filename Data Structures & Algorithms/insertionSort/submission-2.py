# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        if len(pairs) == 0 : 
            return []
        result = [pairs.copy()] # Make a copy 

        for i in range(1, len(pairs)):
            key_pair = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > key_pair.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = key_pair
            result.append(pairs.copy())
            
        return result