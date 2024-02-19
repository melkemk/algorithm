# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # trav=head
        # while trav and trav.next:
        #     if trav.next.val==node.val:
        #         trav.next=trav.next.next
        #         return 
        #     trav=trav.next
        # if trav and trav.val==node.val:
        #     head=head.next
        node.val=node.next.val
        node.next=node.next.next