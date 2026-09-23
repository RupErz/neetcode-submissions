class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Q: what if it have to be insert at the front ?
        result = []
        added = False

        # Insert first
        for i in range(len(intervals)):
            start, stop = intervals[i]
            startinsert, stopinsert = newInterval

            # Check overlap first
            if stop >= startinsert and start <= stopinsert: 
                # Start merging
                mergestart, mergestop = min(start, startinsert), max(stop, stopinsert)
                newInterval = [mergestart, mergestop]
            else:
                # If not overlap then insert whatever smaller starting point
                if stop < startinsert:
                    result.append([start, stop])
                if start > stopinsert:
                    result.append([startinsert, stopinsert])
                    result.append([start, stop])
                    result += intervals[i + 1:]
                    added = True

                    break
                
        if not added:
            result.append(newInterval)
        return result
            


                
