class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = []
        for i,ele in enumerate(nums):
            nums_d.append([ele,i])
        nums_d.sort()
        l,r = 0, len(nums)-1
        while l<=r:
            summ = nums_d[l][0] + nums_d[r][0]
            if summ == target:
                return [min(nums_d[l][1],nums_d[r][1]),max(nums_d[l][1],nums_d[r][1])]
            elif summ > target:
                r-=1
            else:
                l+=1

        