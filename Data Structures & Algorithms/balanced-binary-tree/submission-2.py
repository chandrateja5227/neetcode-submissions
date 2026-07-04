# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True

        if not root:
            return True

        def dfs(node, height):
            if not node:
                return 0

            left = dfs(node.left,height)
            right = dfs(node.right, height)
            height = 1 + max(left,right)   
            Bal = (max(left,right) - min(left,right))
            nonlocal isBal
            if Bal > 1 and isBal:
                isBal = False

            return height

        _ = dfs(root,0)

        return isBal
            
        