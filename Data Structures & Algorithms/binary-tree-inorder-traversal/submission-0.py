# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.inOrder(root,arr)
        return arr



    def inOrder(self,root,arr):    
        if not root:
            return

        self.inOrder(root.left,arr)
        arr.append(root.val)
        self.inOrder(root.right,arr)

        return



        