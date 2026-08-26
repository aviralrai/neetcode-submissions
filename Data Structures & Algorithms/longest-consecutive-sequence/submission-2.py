class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        def search_ele(d: {}, target: int):
            if target in d.keys():
                if d[target] == -1:
                    # print(target)
                    d[target] = 1 + search_ele(d,target+1)
                    return d[target]
                else:
                    return d[target]
            else:
                return 0
        d = {}
        for key in nums:
            d[key] = -1
        # print(d)
        for key,val in d.items():
            # print(key,val)
            if val == -1:
                d[key] = 1 + search_ele(d,key+1)
        # print(d)
        ans = max(d.values())
        return ans