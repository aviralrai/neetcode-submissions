class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            out = x-y
            if out != 0: heapq.heappush(max_heap, out)
        return abs(max_heap[0]) if max_heap else 0


        