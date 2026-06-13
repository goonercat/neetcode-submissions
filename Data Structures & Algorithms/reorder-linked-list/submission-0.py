# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp = head
        fp = head.next

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        l2 = sp.next
        prev = sp.next = None

        #reverse list

        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp

        # merge two

        l1 = head
        l2 = prev

        while l2:
            t1 = l1.next
            t2 = l2.next
            l1.next = l2
            l2.next = t1
            l1,l2 = t1,t2