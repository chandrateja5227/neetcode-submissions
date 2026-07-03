# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        def diameter(node, maxlen, dia):

            if not node:
                return [maxlen , dia]

            left  = diameter(node.left , maxlen, dia)
            right = diameter(node.right , maxlen, dia)
            maxlen = 1 + max(left[0] , right[0])
            node_dia =  left[0] + right[0]
            dia = max(max( left[1] , right[1]) ,node_dia )

            return [maxlen , dia]

        return diameter(root,0,0)[1]
        