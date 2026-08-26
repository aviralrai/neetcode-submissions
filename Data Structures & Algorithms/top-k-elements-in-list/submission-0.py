class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        import heapq
        heap = []
        freq_t = tuple(freq.items())
        # print(freq_t)
        for item,freq in freq_t:
            # print(heap)
            heapq.heappush(heap,(freq,item))
            if len(heap) > k:
                heapq.heappop(heap)
            # print(heap)
        ans = []
        for _,j in heap:
            ans.append(j)
        return ans
        
        