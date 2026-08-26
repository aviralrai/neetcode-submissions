from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        freq_d = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        top_k = []
        for key in freq_d:
            if k == 0:
                return top_k
            top_k.append(key)
            k -= 1
        return top_k

        