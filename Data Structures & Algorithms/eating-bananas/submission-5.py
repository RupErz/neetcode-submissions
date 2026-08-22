class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Sol : since we know our k worst case is max(piles) and k > 1
        # We could make use of this number range 
        # Instead of going through each value , we use BINARY SEARCH
        # If our time is <= h then we can try minimize our k buy move r ptr
        # else we move l ptr to make it suitable k value
        l, r = 1, max(piles)
        # Recap : left & right ptr point at value not index
        res = r # Worst case when res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            if hours <= h :
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

    

        