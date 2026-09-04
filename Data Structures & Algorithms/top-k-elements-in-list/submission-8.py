class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        min_heap = []

        for key,val in freq.items():
            heapq.heappush(min_heap,(val,key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        ans = []

        for val, key in min_heap:
            ans.append(key)
        return ans
        