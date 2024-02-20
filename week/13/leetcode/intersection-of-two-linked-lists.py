# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        di1=set()
        while headA:
            di1.add(headA)
            headA=headA.next
        while headB:
            if headB in di1:
                return headB
            headB=headB.next