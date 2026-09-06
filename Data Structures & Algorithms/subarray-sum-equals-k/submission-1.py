class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        ans = 0
        curr = 0
        for i,ele in enumerate(nums):
            curr += ele
            if curr - k in count:
                ans += count[curr-k]
            count[curr] = count.get(curr,0) + 1
        return ans

        