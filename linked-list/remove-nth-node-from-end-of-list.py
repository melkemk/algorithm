# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = ListNode()
        ans = slow
        slow.next = head
        fast = head

        while True:
            if n == 1:
                while fast and fast.next:  
                    fast = fast.next
                    slow = slow.next
            
                if slow.next:
                    slow.next = slow.next.next

                return ans.next
                
            n-= 1
            fast = fast.next
            
        