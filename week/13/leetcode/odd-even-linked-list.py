# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even=ListNode()
        odd=ListNode()
        ev=even
        od=odd
        trav=head
        i=0
        while trav :
            if i%2:
                odd.next=ListNode(trav.val)
                odd=odd.next
            else:
                even.next=ListNode(trav.val)
                even=even.next
            trav=trav.next
            i+=1
        even.next=od.next
        return ev.next
