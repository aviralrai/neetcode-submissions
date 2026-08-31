class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_l = 0
        seen = set()
        for ele in nums:
            if ele in seen:
                continue
            l = 1
            seen.add(ele)
            nex = ele + 1
            prev = ele - 1
            while nex in nums_set and nex not in seen:
                seen.add(nex)
                nex += 1
                l += 1
            while prev in nums_set and prev not in seen:
                seen.add(prev)
                l += 1
                prev -= 1
            max_l = max(max_l,l)
        return max_l
        