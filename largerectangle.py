class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxres = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                stacki, stackh = stack.pop()
                maxres = max(maxres,(i-stacki) * stackh)
                start =  stacki
            stack.append((start,h))
        
        for i, h in stack:
            maxres = max(maxres, h*(len(heights) - i))
        return maxres