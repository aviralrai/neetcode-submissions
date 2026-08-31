class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        num_s = sorted(nums)
        for i in range(len(num_s)-2):
            if i != 0 and num_s[i] == num_s[i-1]:
                continue
            l = i + 1
            r = len(num_s) - 1
            target = -1 * num_s[i]
            while l < r:
                summ = num_s[l] + num_s[r]
                if target == summ:
                    ans.append([num_s[i],num_s[l],num_s[r]])
                    l += 1
                    r -= 1
                    while l < r and num_s[l] == num_s[l-1]:
                        l += 1
                    while l < r and num_s[r] == num_s[r+1]:
                        r -= 1
                elif target > summ:
                    l += 1
                else:
                    r -= 1
        return ans
             