class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        res = 0
        curr = 0
        for x in nums:
            curr += x
            res += counts.get(curr - k,0)
            counts[curr] = counts.get(curr,0) + 1
        return res
        