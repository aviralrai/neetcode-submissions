class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x,y in points:
            dist = x*x + y*y
            heapq.heappush(max_heap,(-1*dist,[x,y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        out = []
        while max_heap:
            _,point = heapq.heappop(max_heap)
            out.append(point)
        return out
        