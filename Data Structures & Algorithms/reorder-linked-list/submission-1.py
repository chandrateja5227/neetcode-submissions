# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next == None:
            return None
        stack = []
        left = head
        curr = left.next
        right = head
        while right:
            stack.append(right)
            right = right.next

        while curr and curr.next:
            prev = stack[-2] if stack[-2] else None
            if prev:
                prev.next = None
            node = stack.pop()
            left.next = node
            node.next = curr
            left = curr
            curr = curr.next
