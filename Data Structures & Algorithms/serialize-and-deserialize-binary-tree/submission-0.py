# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        string = ""
        def dfs(root):
            nonlocal string
            if not root:
                string = string + '#' + "_" 
                return 
            string = string  + str(root.val) +  "_"
            dfs(root.left)
            dfs(root.right) 
            
            return 
        dfs(root)
        print(string)
        return string

                   
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:


        arr = data.split("_")

        def dfs(string):
            i = arr.pop(0)
            if i == '#':
                return None
            if i:
                node = TreeNode(int(i),dfs(string), dfs(string)) 

            return node

        
           

        return dfs(data)


            


        
