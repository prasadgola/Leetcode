class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = []

        def dfs(root,comb):
            if len(comb) == len(nums):
                return

            res.append(comb[:])
            for i in range(len(root)):
                comb.append(root[i])
                print(comb)
                dfs(root[i+1:],comb)
                comb.pop()
            
        dfs(nums,[])
        res.append(nums)
        return res