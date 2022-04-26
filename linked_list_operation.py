#create new node
class node:
    def __init__(self,val):
        self.data=val
        self.next=None

#lined list operation
class LL:
    def __init__(self):
        self.head=None
    #insertion at begenning
    def insert_beg(self,val):
        NN=node(val)
        if self.head is None:
            self.head=NN
            return
        NN.next=self.head
        self.head=NN
    #insertion at end
    def insert_end(self,val):
        NN=node(val)
        if self.head is None:
            self.head=NN
            return
        tmp=self.head
        while tmp.next is not None:
            tmp=tmp.next
        tmp.next=NN
    #delete at begin
    def del_beg(self):
        if self.head is None:
            return
        tmp=self.head
        self.head=self.head.next
        tmp.next=None
    #delete at end
    def del_end(self):
        if self.head is None:
            return
        tmp=self.head
        while tmp.next.next is not None:
            tmp=tmp.next
        tmp.next=None
    #print linked list
    def printLL(self,tmp):
        while tmp is not None:
            print(tmp.data,end=" -->")
            tmp=tmp.next

lis=LL()
print("new linked list by instering new node at begenning")
lis.insert_beg(5)
lis.insert_beg(4)
lis.insert_beg(3)
lis.printLL(lis.head)
print("\nlist after deleting some node from begenning")
lis.del_beg()
lis.del_beg()
lis.printLL(lis.head)
print("\nlist after adding new node at end")
lis.insert_end(5)
lis.insert_end(4)
lis.insert_end(3)
lis.printLL(lis.head)
print("\nlist after deleting new node at end")
lis.del_end()
lis.del_end()
lis.printLL(lis.head)