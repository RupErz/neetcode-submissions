# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.recursiveSort(pairs, 0, len(pairs) - 1)

    # Sort 2 half and return the pivot
    def partition(self, arr, low, high):
        pivot = arr[high].key
        # We having 2 index : 1 to move and 1 to swap
        # i start at low - 1, j start at low
        i = low - 1

        for j in range(low, high + 1):
            if arr[j].key < pivot:
                i += 1
                if j > i:
                    arr[i], arr[j] = arr[j], arr[i]
        # index i: pointing to the smallest element to pivot
        # Swap pivot with current i + 1 at the end
        # Because i + 1 is either >= to pivot => Smaller - Pivot - Greater
        arr[high], arr[i + 1] = arr[i + 1], arr[high]
        return i + 1

    def recursiveSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.recursiveSort(arr, low, pi - 1)
            self.recursiveSort(arr, pi + 1, high)
        return arr
        
            