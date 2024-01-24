class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
    def get(self, i: int) -> int:
        trav=self.head
        while trav and i:
            i-=1
            trav=trav.next
            # print(trav.val)
        if trav:
            return trav.val
        else:return -1
    def addAtHead(self, val: int) -> None:
        n=Node(val)
        n.next=self.head
        self.head=n
    def addAtTail(self, val: int) -> None:
        trav=self.head 
        if not trav:
            self.head=Node(val)
            print(self.get(0))
            return

        while  trav.next :
            trav=trav.next
        trav.next=Node(val) 
    def addAtIndex(self, i: int, val: int) -> None:
        if i==0:  
            self.addAtHead(val)
        else:
            trav=self.head
            while trav and trav.next and i-1:
                i-=1
                trav=trav.next
            temp=Node(val)
            if trav:
                temp.next=trav.next
                trav.next=temp
            else:
                trav=temp
            print(self.get(i))
    def deleteAtIndex(self, i: int) -> None: 
        trav=self.head  
        if not trav:return
        if i==0 and trav:
            trav=trav.next
            self.head=trav
        for j in range(i-1):
            if not trav:return
            trav=trav.next
        if trav and trav.next:
            if trav.next.next:
                trav.next=trav.next.next
            else:trav.next=None

            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(0)
# obj.addAtHead(38)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# print(param_1)
