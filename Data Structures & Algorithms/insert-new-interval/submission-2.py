class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        lo, hi = 0, len(intervals)
        target = newInterval[0]
        while lo<hi:
            mid = (lo+hi)//2
            if target <= intervals[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        intervals.insert(lo,newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
        