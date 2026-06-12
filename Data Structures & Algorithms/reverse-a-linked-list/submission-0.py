# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pr = None
        cu = head
        while cu:
            nxt = cu.next
            cu.next = pr
            pr = cu
            cu = nxt

        return pr