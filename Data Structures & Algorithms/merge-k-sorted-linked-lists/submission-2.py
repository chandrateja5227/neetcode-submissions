class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergek(lists, 0, len(lists) - 1)

    def mergek(self, lists, start, end):
        if start == end:
            return lists[start]
        if start > end:
            return None

        m = (start + end) // 2
        left = self.mergek(lists, start, m)
        right = self.mergek(lists, m + 1, end)
    
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left is not None and right is not None:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next