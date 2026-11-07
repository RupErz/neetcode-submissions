class TimeMap:

    def __init__(self):
        self.timer = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timer[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.timer[key]:
            return self.timer[key][timestamp]
        else:
            cur = timestamp - 1

            # I notice this part is weird but cant help
            while cur >= 0:
                if cur in self.timer[key]:
                    return self.timer[key][cur]
                cur -= 1
            return ""

    #     alice: {
    #         1: happy,
    #         3: sad
    #     }


    # quang dang