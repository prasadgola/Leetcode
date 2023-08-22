class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root,comb):
            if not root:
                return ''
            
            comb += str(root.val)+"->"
            dfs(root.left,comb)
            dfs(root.right, comb)
            if not root.left and not root.right:
                res.append(comb[:-2])
        dfs(root,'')
        return res