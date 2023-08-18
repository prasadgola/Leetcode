class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left, depth +1 ])
                stack.append([node.right,depth + 1])
        return res