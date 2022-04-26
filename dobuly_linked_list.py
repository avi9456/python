class node:
    def __init__(self,val):
        self.pre=None
        self.data=val
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_beg(self,val):
        NN=node(val)
        if self.head is None:
            self.head=NN
            return
        NN.next=self.head
        self.head.pre=NN
        self.head=NN
    def insert_end(self,val):
        NN=node(val)
        if self.head is None:
            self.head=NN
        tmp=self.head
        while tmp.next is not None:
            tmp=tmp.next
        tmp.next=NN
        NN.pre=tmp
    def printDLL(self,head):
        while head is not None:
            print(head.data,end=" ")
            last=head
            head=head.next
        while last is not None:
            print(last.data,end=" ")
            head=last
            last=last.pre
dlist=DLL()
print("insert at the begining of list")
dlist.insert_beg(5)
dlist.insert_beg(4)
dlist.insert_beg(3)
dlist.insert_beg(2)
dlist.insert_beg(1)
dlist.printDLL(dlist.head)
print("\ninsert at the end of list")
dlist.insert_end(6)
dlist.insert_end(7)
dlist.insert_end(8)
dlist.insert_end(9)
dlist.insert_end(0)
dlist.printDLL(dlist.head)