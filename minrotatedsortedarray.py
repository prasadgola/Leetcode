class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        l,h = 0, len(nums) - 1

        if nums[l]<nums[h] or h==0:
            print(l,h)
            return nums[0]
        if h==1:
            return nums[1]

        while l < h:
            mid = (l + h) // 2
            print(l,mid,h)
            if nums[mid] > min:
                # min = nums[l]
                l = mid + 1
            elif nums[mid] < min:
                h = mid
                min = nums[h]
        return nums[l]