class TimeMap:

    def __init__(self):
        self.time = {}
        self.timestamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[(key,timestamp)] = value
        self.timestamps[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
            times = self.timestamps[key]
            lo, hi = 0, len(times)
            while lo < hi:
                mid = (lo+hi)//2
                if times[mid] > timestamp:
                    hi = mid
                else: lo = mid + 1
            return self.time[(key,times[lo-1])] if lo > 0 else ""

