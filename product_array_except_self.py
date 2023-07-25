class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = []
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]*nums[i])
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums) - 1:
                postfix.append(nums[j])
            else:
                # print(len(nums)-j-2)
                postfix.append(postfix[len(nums)-j-2]*nums[j])
        postfix = postfix[::-1]
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[1])
            elif i == len(nums)-1:
                output.append(prefix[len(prefix) -2])
            else:
                output.append(prefix[i-1]*postfix[i+1])
        return output