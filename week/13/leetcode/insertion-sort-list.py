# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val  =  val
#         self.next  =  next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        ans=[]
        while trav:
            ans.append(trav.val)
            trav=trav.next
        ans.sort()
        tr=ListNode()
        anss=tr
        for i in ans:
            tr.next=ListNode(i)
            tr=tr.next
        return anss.next