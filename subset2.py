class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res  = []
        nums.sort()
        def dfs(root,comb):
            if len(comb) == len(nums):
                return
            
            if comb not in res:
                res.append(comb.copy())
            for i in range(len(root)):
                comb.append(root[i])
                dfs(root[i+1:],comb)
                comb.pop()
            
        dfs(nums,[])
        res.append(nums)
        return res