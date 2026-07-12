# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        string = []
        def dfs(root):
            if not root:
                return string.append("#")

            string.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)
        res = '_'.join(string)
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        string = data.split("_")
        def dfs(root):
            value = string.pop(0)
            if value == "#":
                return None

            return TreeNode(value,dfs(root.left), dfs(root.right))

        return dfs(root)












