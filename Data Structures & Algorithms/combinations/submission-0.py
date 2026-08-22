class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curSubset = []
        result = []

        def helper(i, curSubset, result, n, k):
            if len(curSubset) == k:
                result.append(curSubset.copy())
                return
            
            if i > n:
                return

            for j in range(i, n + 1):
                curSubset.append(j)
                helper(j + 1, curSubset, result, n, k)
                curSubset.pop()



        helper(1, curSubset, result, n, k)
        return result