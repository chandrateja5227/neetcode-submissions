class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, max_val):
            if not root:
                return
            nonlocal count
            if max_val <= root.val:
                max_val = root.val
                count += 1
            dfs(root.left, max_val)
            dfs(root.right, max_val)

            return
        dfs(root, root.val)
        return count