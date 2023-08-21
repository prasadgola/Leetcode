class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        def dfs(root):
            if not root:
                return
            lis.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return lis