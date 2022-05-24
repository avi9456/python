from ast import Not


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
            print(f"{NN.data} is inserted at begging")
            return
        NN.next=self.head
        self.head.pre=NN
        self.head=NN
        print(f"{NN.data} is inserted at begging")
    def insert_end(self,val):
        NN=node(val)
        if self.head is None:
            self.head=NN
        tmp=self.head
        while tmp.next is not None:
            tmp=tmp.next
        tmp.next=NN
        NN.pre=tmp
        print(f"{NN.data} is inserted at end")
    def insert_after(self,nod,data,pos):
        NN=node(data)
        if self.head is None:
            self.head=NN
        else:
            p=1
            while nod:
                pre=nod
                nod=nod.next
                p=p+1
                if p==pos:
                    break
            pre.next=NN
            NN.pre=pre
            NN.next=nod
    def deletafter(self,key):
        temp=self.head
        if self.head is None:
            print("list is empty")
        else:
            if temp.data==key:
                self.head=temp.next
                self.head.pre=None
                temp=None
                return
            while temp is not None:
                if temp.data==key:
                    temp.next.pre=temp.pre
                    temp.pre.next=temp.next
                    temp=None
                else:
                    temp=temp.next
    def del_beg(self):
        if self.head is None:
            print("list is empty")
        else:
            tmp=self.head
            self.head=self.head.next
            self.head.pre=None
            print(f"{tmp.data} is deleted")
    def del_end(self):
        if self.head is None:
            print("list is empty")
        else:
            tmp=self.head
            while tmp.next.next is not None:
                tmp=tmp.next
            tmp2=tmp.next
            tmp.next=None
            tmp2.pre=None
            print(f"{tmp2.data} is deleted")
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
dlist.insert_beg(5)
dlist.insert_beg(4)
dlist.insert_beg(3)
dlist.insert_beg(2)
dlist.insert_beg(1)
dlist.insert_after(dlist.head,30,2)
dlist.printDLL(dlist.head)
print()
dlist.del_beg()
dlist.del_beg()
dlist.insert_end(6)
dlist.insert_end(7)
dlist.insert_end(8)
dlist.insert_end(9)
dlist.insert_end(0)
dlist.del_end()
dlist.del_end()
dlist.deletafter(4)
dlist.printDLL(dlist.head)