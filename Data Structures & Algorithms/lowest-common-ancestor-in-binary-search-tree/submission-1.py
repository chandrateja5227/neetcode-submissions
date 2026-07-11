# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        res = [root]

        def dfs(root,p , q):
            if not root:
                return 
            
            if max(p.val,q.val) < root.val:
                dfs(root.left,p , q) 
            elif min(p.val,q.val) > root.val:
                dfs(root.right,p , q) 
            else: 
                res[0] = root

            return
        dfs(root,p,q)
        return res[0]

