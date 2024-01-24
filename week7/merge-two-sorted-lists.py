# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=None
        newNode=ans
        while list1 and list2:
            if list1.val>list2.val:
                if not newNode:
                    newNode=ListNode(list2.val)
                    ans=newNode
                else:
                    newNode.next=ListNode(list2.val)
                    newNode=newNode.next
                list2=list2.next
            else:
                if not newNode:
                    newNode=ListNode(list1.val)
                    ans=newNode
                else:
                    newNode.next=ListNode(list1.val)
                    newNode=newNode.next
                list1=list1.next
        if list1:
            if not newNode:
                newNode=list1
                ans=newNode
            else:
                newNode.next=list1
        if list2:
            if not newNode:
                newNode=list2
                ans=newNode
            else:
                newNode.next =list2

        return ans
        