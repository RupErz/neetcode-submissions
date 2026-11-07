class TimeMap:

    def __init__(self):
        self.timer = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timer[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.timer.get(key, [])
        l, r = 0, len(pairs) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            time, val = self.timer[key][mid]
            if time <= timestamp:
                result = val
                l = mid + 1
            else:
                r = mid - 1
        return result 

