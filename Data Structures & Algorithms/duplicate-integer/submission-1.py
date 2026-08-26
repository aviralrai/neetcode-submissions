class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = dict()
        for i in range(len(nums)):
            if nums[i] in has.keys() and has[nums[i]] == True:
                return True
            has[nums[i]] = True
        return False
        