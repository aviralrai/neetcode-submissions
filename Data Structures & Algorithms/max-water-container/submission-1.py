class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_Area = 0
        l = 0
        r = len(heights)-1
        while l<r:
            area = min(heights[l],heights[r]) * (r-l)
            if area > max_Area:
                max_Area = area
            if heights[l] >= heights[r]:
                r-=1
            else: l+=1
        return max_Area
        