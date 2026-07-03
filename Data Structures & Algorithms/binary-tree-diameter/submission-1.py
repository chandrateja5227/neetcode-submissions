# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        dia = 0
        def diameter(node, maxlen):

            if not node:
                return 0

            left  = diameter(node.left , maxlen)
            right = diameter(node.right , maxlen)
            maxlen = 1 + max(left , right)
            node_dia =  left + right
            nonlocal dia
            dia = max(dia ,node_dia)

            return maxlen 
        diameter(root,0)
        return dia
        