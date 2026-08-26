class Solution:
    def trap(self, height: List[int]) -> int:
        right_max = [0] * len(height)
        r_max = height[-1]
        for i in range(len(height)-2,-1,-1):
            if r_max > height[i]:
                right_max[i] = r_max
            else:
                r_max = height[i]
        max_l = 0
        ans = 0
        # print(right_max)
        for i in range(len(height)-1):
            if max_l <= height[i]:
                max_l = height[i]
                continue
            else:
                trap = min(max_l,right_max[i])
                if trap > 0:
                    trap -= height[i]
                ans += trap
        return ans


        