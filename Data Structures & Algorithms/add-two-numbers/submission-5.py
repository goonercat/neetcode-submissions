# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sm = 0
        h1 = l1
        i = 0
        while not h1 == None:
            sm += h1.val *(10**i)
            i+=1
            h1 = h1.next
        h2 = l2
        i = 0
        while not h2 == None:
            sm += h2.val *(10**i)
            i+=1
            h2 = h2.next
        if sm == 0:
            return ListNode(0)
        hd = ListNode()
        l3 = hd
        while sm > 0:
            dx = ListNode(sm%10)
            l3.next = dx
            l3 = dx
            sm //= 10
        return hd.next