# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p,q):

            if p and q:
                left = dfs(p.left , q.left)
                right = dfs(p.right , q.right)
                if (left and right) and p.val == q.val:
                    return True
                else:
                    return False

            elif p == q:
                return True
            else:
                return False
            

            

        return dfs(p,q)


             
        