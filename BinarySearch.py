class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            median = (right + left) // 2
            if nums[median] == target:
                return median
            if left == right:
                return -1
            if target <= nums[median]:
                right = median
            else:
                left = left + 1 if left == median else median
        return -1