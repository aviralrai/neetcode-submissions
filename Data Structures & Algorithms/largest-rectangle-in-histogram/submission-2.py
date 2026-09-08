class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                w,h = stack.pop()
                area = (i-w)*h
                maxArea = max(area,maxArea)
                start = w
            stack.append((start,heights[i]))
        end = len(heights)
        for start, h in stack:
            area = (end-start) * h
            maxArea = max(area,maxArea)
        return maxArea