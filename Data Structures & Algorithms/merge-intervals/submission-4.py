class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # This time the list has not been sorted 

        result = []
        intervals.sort()

        for curStart, curStop in intervals:
            if len(result) == 0:
                result.append([curStart, curStop])
                continue
            
            prevStart, prevStop = result[-1]

            # Check for merge conditions: 
            if prevStop >= curStart and prevStart <= curStop:
                insertedStart, insertedStop = min(prevStart, curStart), max(prevStop, curStop)
                result.pop()
                result.append([insertedStart, insertedStop])
            else:
                result.append([curStart, curStop])
        
        return result