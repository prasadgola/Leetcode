class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        while True:
            val = numbers[i] + numbers[j]
            if val == target:
                return [i+1,j+1]
            if val > target:
                j = j - 1
            else:
                i = i + 1