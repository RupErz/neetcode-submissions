class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Perform binary search right on the number from 1 to max
        l, r = 1, max(piles)
        res = r # The worst case res is equal to r (max)
        while l <= r:
            k = ( l + r) // 2
            hours = 0
            for p in piles :
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else :
                l = k + 1
        return res


    

        