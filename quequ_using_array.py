class queue:
    def __init__(self,c):
        self.queue=[]
        self.front=self.rear=0
        self.capacity=c
    def enqueue(self,data):
        if self.capacity==self.rear:
            print("queue is full")
        else:
            self.queue.append(data)
            self.rear+=1
            print(f"{data} is enqueue")
    def dequeue(self):
        if self.front==self.rear:
            print("queue is empty")
        else:
            x=self.queue.pop(0)
            self.rear-=1
            print(f"{x} is dequeue")
    def dispaly(self):
        if self.front==self.rear:
            print("queue is empty")
        for i in self.queue:
            print(f"{i} --",end=" ")
if __name__=='__main__':
    q=queue(3)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.dispaly()
    print()
    q.dequeue()
    q.dispaly()