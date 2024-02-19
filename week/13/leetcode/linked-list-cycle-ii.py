# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        intersection=None
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                intersection=slow
                break
        if not intersection:return None
        i=0
        trav=head
        while trav!=intersection:
            trav=trav.next
            intersection=intersection.next
        return trav

        

