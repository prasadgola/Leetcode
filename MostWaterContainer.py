class Solution:
    def maxArea(self, height: List[int]) -> int:
        tuples = []
        areas = []
        i,j = 0,len(height)-1
        while i < j:
            if height[i] < height[j]:
                areas.append(height[i]*(j-i))
                i = i + 1
                print
            else:
                areas.append(height[j]*(j-i))
                j = j - 1
        return max(areas)