class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    

        if not root:
            return False
        
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

        if match(root , subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)