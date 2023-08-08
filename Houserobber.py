class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            if not dp:
                dp.append(nums[i])
                continue
            if len(dp) == 1:
                dp.append(max(dp[i-1],nums[i]))
            else:
                dp.append(max(dp[i-1],dp[i-2] + nums[i]))
        return dp[-1]