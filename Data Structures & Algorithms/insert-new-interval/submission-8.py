class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Optimal : Time: O(N), Space: O(1)
        result = []
        added = False
        startinsert, stopinsert = newInterval

        for start, stop in intervals:
            # This is totally smaller than newInterval
            if stop < startinsert:
                # Only insert this
                result.append([start, stop])
            elif start <= stopinsert: # if it start overlap
                startinsert, stopinsert = min(start, startinsert), max(stop, stopinsert)
            else: # The current pair is way higher than inserted
                # Insert the new interval if hasnt
                if not added:
                    result.append([startinsert, stopinsert])
                    added = True
                result.append([start, stop])
        if not added:
            result.append([startinsert, stopinsert])
        return result
