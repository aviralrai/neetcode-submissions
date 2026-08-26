class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_ele = {}
        for i,ele in enumerate(nums):
            diff = target - ele
            if diff in pre_ele:
                return [pre_ele[diff],i]
            pre_ele[ele] = i 

        