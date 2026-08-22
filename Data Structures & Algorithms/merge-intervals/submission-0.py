class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for i in range(len(intervals)):
            if i == 0 :
                result.append([intervals[i][0], intervals[i][1]])
                continue
            # Compare with last appended value [-1]
            endFirst = result[-1][1]
            startFirst = result[-1][0]

            startSecond = intervals[i][0]
            endSecond = intervals[i][1]

            # Checking for merge condition :
            if endFirst >= startSecond :
                minRange = startFirst
                maxRange = max(endFirst, endSecond)
                result.pop()
                result.append([minRange, maxRange])
            else :
                result.append([startSecond, endSecond])
        return result 

    # [1, 2]
        
        # Sort : compare 1st value, if equal, start compare 2nd value

        # Merge : first end >= second start : Merge

        # stack: [1, 3], [4, 5], [2, 6]
        # [1, 3], [7, 9], [2, 6]
        # => [1, 3], [2, 6], [7, 9], [8, 10]
        # [1, 6], [7,9]