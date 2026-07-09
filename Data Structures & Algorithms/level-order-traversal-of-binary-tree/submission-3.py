# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = my_queue = deque()

        list = []
        if root:
            queue.append(root)

        level = 0

        while len(queue) > 0:
            sublist = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    sublist.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            level +=1
            list.append(sublist)

        return list



            
        