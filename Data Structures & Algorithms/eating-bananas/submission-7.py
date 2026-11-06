import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        # if h == len(piles):
        #     return piles[-1]

        l, r = 1, piles[-1]
        rate = 0 # 0 as fallback value
        while l <= r:
            mid = (l + r) // 2

            # Check if this is a right rate
            total = 0
            for p in piles:
                total += (math.ceil(p / mid))

            if total > h:
                l = mid + 1
            else:
                rate = mid
                r = mid - 1
        
        return rate



        
        