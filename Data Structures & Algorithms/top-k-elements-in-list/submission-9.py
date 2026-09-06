class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = Counter(nums)
        freq  = [[] for _ in range(len(nums)+1)]

        for key, val in count.items():
            freq[val].append(key)
        ans  = []
        for ele in reversed(freq):
            for num in ele:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return []

        