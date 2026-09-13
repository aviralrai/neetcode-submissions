class TimeMap:

    def __init__(self):
        self.time = {}
        self.timestamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[(key,timestamp)] = value
        self.timestamps[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if (key,timestamp) in self.time:
            return self.time[(key,timestamp)]
        elif key not in self.timestamps:
            return ""
        elif timestamp < self.timestamps[key][0]:
            return ""
        else:
            times = self.timestamps[key]
            lo, hi = 0, len(times)
            while lo < hi:
                mid = (lo+hi)//2
                if times[mid] < timestamp:
                    if lo == mid:
                        break
                    lo = mid
                else: hi = mid
            return self.time[(key,times[lo])] if lo < len(times) else self.time[(key,times[-1])]

