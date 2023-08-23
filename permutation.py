class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(newnums, comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            
            for i in range(len(newnums)):
                comb.append(newnums[i])
                dfs(newnums[:i] + newnums[i+1:], comb)
                comb.pop()
        
        dfs(nums,[])
        return res