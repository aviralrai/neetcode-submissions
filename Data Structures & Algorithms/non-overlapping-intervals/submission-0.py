class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        keep, last = 0, float('-inf')
        for start, end in intervals:
            if start >= last:
                keep+=1
                last = end
        return len(intervals) - keep
        
        