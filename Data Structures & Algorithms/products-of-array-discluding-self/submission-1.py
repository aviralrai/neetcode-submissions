class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = 1 
        right_prod = [1]
        prod = 1
        ans = []
        for i in range(len(nums)-1,0,-1):
            prod *= nums[i]
            right_prod.append(prod) #[1,6,24,48]

        for l in range(len(nums)):
            if l != 0:
                l_prod *= nums[l-1]
            ans.append(l_prod*right_prod[len(nums)-1-l])
        
        return ans
            
            
        