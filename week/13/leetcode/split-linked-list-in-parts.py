# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        trav = head
        while trav:
            trav = trav.next
            length += 1
        total = length//k
        rem = length%k
        trav = head
        ans = []
        while trav :
            temp = total+1 if rem else total
            if rem :rem-=1
            partial = ListNode(0)
            partialans = partial
            while temp and trav:
                k-=1
                temp -= 1
                partial.next = ListNode(trav.val)
                trav = trav.next
                partial = partial.next
            ans.append(partialans.next)
        while  k>0:
            k-=1
            print(k)
            ans.append(ListNode(0).next)
        return ans