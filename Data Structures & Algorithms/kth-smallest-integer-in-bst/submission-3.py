# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        
        result = root.val
        count = k
        def dfs(root,k):
            if not root:
                return 
            nonlocal result ,count

            dfs(root.left,k)
            if count == 0:
                return

            count-=1    

            if count == 0:
                result = root.val
                return

            right = dfs(root.right,k)

            return 

        
        _ = dfs(root,k)

        return result

        