class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mp = {value: index for index, value in enumerate(inorder)}

        return self.bst(mp,preorder, 0,len(preorder)-1,inorder,0,len(inorder)-1)


    def bst(self,mp,preorder,prestart,preend,inorder,instart,inend):
        if prestart > preend or instart > inend:
            return None

        root = TreeNode(preorder[prestart])
        index = mp.get(preorder[prestart])
        numsLeft = index - instart

        root.left = self.bst(mp,preorder, prestart+1, prestart+numsLeft, inorder, instart, index-1)
        root.right = self.bst(mp,preorder, prestart+numsLeft+1, preend, inorder, index+1, inend)

        return root