class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        ans = []
        for i in range(len(nums_sort)-2):
            target = -1 * nums_sort[i]
            l = i + 1
            r = len(nums_sort)-1
            while l < r:
                if nums_sort[l] + nums_sort[r] == target:
                    ans.append([nums_sort[i],nums_sort[l],nums_sort[r]])
                    l+=1
                    r-=1
                elif nums_sort[l] + nums_sort[r] < target:
                    l += 1
                else: r -= 1
        unique_data = [list(item) for item in {tuple(sublist) for sublist in ans}]
        return unique_data
        