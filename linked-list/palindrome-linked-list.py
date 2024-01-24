# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
       curr=head
       t=deepcopy(head)
       prev=None
       while curr:
           temp=curr.next
           curr.next=prev
           prev=curr
           curr=temp
       while prev:
           if prev.val!=t.val:return False
           prev=prev.next
           t=t.next
       return 1