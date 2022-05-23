class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def isempty(self):
        return(self.front==None)
    def enqueue(self,data):
        NN=node(data)
        if self.rear==None:
            self.front=self.rear=NN
            print(f"{NN.data} is enqueued")
            return
        self.rear.next=NN
        self.rear=NN
        print(f"{NN.data} is enqueued")
    def dequeue(self):
        if self.isempty():
            return
        tmp=self.front
        self.front=tmp.next
        if self.front==None:
            self.rear=None
if __name__=='__main__':
    q=queue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print("queue front"+str(q.front.data))
    print("queue rear"+str(q.rear.data))
    q.dequeue()
    print("queue front"+str(q.front.data))
    print("queue rear"+str(q.rear.data))
    q.dequeue()
    print("queue front"+str(q.front.data))
    print("queue rear"+str(q.rear.data))
