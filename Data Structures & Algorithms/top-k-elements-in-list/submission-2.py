class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = defaultdict(int)
        for n in nums:
            count_nums[n] += 1
        freq = defaultdict(list)
        for key, val in count_nums.items():
            freq[val].append(key)
        ans = []
        for i in range(len(nums),-1,-1):
            if not freq[i]:
                continue
            ans.extend(freq[i])
            k -= len(freq[i])
            if k <= 0:
                break
        return ans

        