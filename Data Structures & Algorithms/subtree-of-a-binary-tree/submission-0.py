# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = False
        def match(parentNode, childNode):
            if not childNode and not parentNode:
                return True

            if childNode and parentNode and parentNode.val == childNode.val:
                if match(parentNode.left,childNode.left) and match(parentNode.right,childNode.right):
                    return True
                else:
                    return False
            else:
                return False

        def dfs(treeNode, subroot):

            if not treeNode:
                return

            nonlocal result
 
            if not result:
                tmp = match(treeNode,subroot)
                if tmp:
                    result = tmp

            dfs(treeNode.left,subroot)
            dfs(treeNode.right,subroot)

            return
        dfs(root,subRoot)

        return result

        














                    
        