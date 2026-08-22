class TimeMap:
    # map { key : [[time, val], [time, val] , [time, val]]}
    # How do we find the correct val with key and time stamp ?
    # => Binary search ) O(logN)
    def __init__(self):
        self.store = {} # key : [ [val, time] ]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] 
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) # case user get an invalid key

        #binary search
        l, r = 0, len(values) - 1
        while l <= r :
            m = ( l + r ) // 2
            if values[m][1] <= timestamp : # As long as it less than or = wecan store it
                res = values[m][0]
                l = m + 1
            else : # greater timestamp => not valid
                r = m - 1
        return res
        # mapList = self.mapKey[key]
        # l, r = 0, len(mapList) - 1
        # while l <= r :
        #     m = (l + r) // 2
        #     if mapList[m][0] == timestamp:
        #         self.recentVal = mapList[m][1]
        #         return self.recentVal
            
        #     if mapList[m][0] > timestamp :
        #         r = m - 1
        #     else :
        #         l = m + 1
        # return self.recentVal

