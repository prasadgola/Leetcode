class Solution:
    def trap(self, height: List[int]) -> int:
        units = []
        for i in range(1,len(height)-1):
            left = max(height[0:i])
            right = max(height[i:len(height)])
            unit = min(left,right)-height[i]
            if unit > -1:
                units.append(unit)
        return sum(units)