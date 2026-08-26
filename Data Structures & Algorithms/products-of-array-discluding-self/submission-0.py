class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]
        for i in nums[0:len(nums)-1]:
            left_prod.append(left_prod[-1] * i)
        print(left_prod)
        right_prod = 1
        ans = []
        for i in range(len(nums)-1,-1,-1):
            ans.append(left_prod[i]*right_prod)
            right_prod *= nums[i]
        return list(reversed(ans))
            
        