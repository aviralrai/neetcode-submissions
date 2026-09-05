class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        ans = 0
        l_h = 0
        for i in range(len(height)):
            if i == 0:
                continue
            left[i] = max(l_h,height[i-1])
            l_h = left[i]
        r_h = 0
        for i in range(len(height)-1,-1,-1):
            if i == len(height) - 1:
                continue
            right[i] = max(r_h,height[i+1])
            r_h = right[i]
        for i in range(len(height)):
            h = min(left[i],right[i]) - height[i]
            ans += max(h,0)
        return ans
                

            
                

        