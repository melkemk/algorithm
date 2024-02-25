class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        previous,curr = dummy,head
        
        for _ in range(left - 1):
            previous = previous.next
            curr = curr.next
        prev = None
        for _ in range(right - left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        previous.next.next = curr
        previous.next = prev
        return dummy.next