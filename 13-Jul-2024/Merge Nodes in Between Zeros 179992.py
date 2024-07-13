# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        trav,temp,head = ans,0,head.next
        while head:
            if head.val==0:
                trav.next = ListNode(temp)
                trav = trav.next 
                temp = 0  
            else:temp +=head.val
            head = head.next
        return ans.next
        
