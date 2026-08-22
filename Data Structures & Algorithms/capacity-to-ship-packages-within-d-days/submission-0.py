class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minRange = max(weights)
        maxRange = sum(weights)

        def isValid(num):
            daysPassed = 1 # To avoid case when loop end curWeight still at n and hasnt progress
            curWeight = 0 
            for i in weights:
                if curWeight + i > num:
                    daysPassed += 1
                    curWeight = 0
                curWeight += i
            
            return True if daysPassed <= days else False 

        l, r = minRange, maxRange
        result = maxRange
        while l <= r:
            mid = (l + r) // 2

            if isValid(mid):
                result = min(result, mid)
                r = mid - 1
            else: 
                l = mid + 1
        
        return result






            # [5, 15] - Min: Least can have to work , 15 max can have
            # [5, 6, ...., 15]
            # Within this range, find the minimal val that will result 
            # But ? Isnt smallest weigh available is 5 ? oh the days limit comes in

            # Try at the middle with Binary Search
            # If it works, we move to left otherwise move to right until invalid.

            # How do you determine if it works?
            # Increment one by one through the list until n days