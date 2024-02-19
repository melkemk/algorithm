# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], t: int) -> Optional[ListNode]:
        x=ListNode()
        trav=head
        ans=x
        while trav:
            if trav.val<t:
                x.next=ListNode(trav.val)
                x=x.next
            trav=trav.next
        trav=head
        while trav:
            if trav.val>=t:
                x.next=ListNode(trav.val)
                x=x.next
            trav=trav.next
        return ans.next