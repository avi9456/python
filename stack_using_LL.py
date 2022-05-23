class stacknode:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        NN=stacknode(data)
        if self.head is None:
            self.head=NN
        else:
            NN.next=self.head
            self.head=NN
        print(f"{NN.data} is pushed")
    def pop(self):
        if self.head is None:
            print("stack is empty")
        else:
            tmp=self.head
            self.head=self.head.next
            print(f"{tmp.data} is deleted")
    def peek(self):
        if self.head is None:
            print("stack is empty")
        else:
            print(f"{self.head.data}")
stack1=stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.peek()
stack1.pop()
stack1.peek()
stack1.pop()
stack1.peek()
stack1.pop()
stack1.peek()