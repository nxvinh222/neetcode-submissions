# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = ListNode(-1, head)
        right = left

        while n > 0:
            right = right.next
            n += -1

        while right:
            if not right.next:
                if left.next == head:
                    return head.next
                left.next = left.next.next
                return head

            left = left.next
            right = right.next

        return head
        