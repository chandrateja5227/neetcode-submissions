# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        

        def depth(node,count):
            if not node:
                return count
            
            count += 1 + max(depth(node.left,count),depth(node.right,count))

            return count

        return depth(root,0)

        
