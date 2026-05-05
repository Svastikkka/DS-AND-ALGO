class QueueUsingArray:
    def __init__(self):
        self.arr=[]
        self.count=0
        self.front=0
        self.rear=0
    def EnQueue(self,num):
        self.arr.append(num)
        self.count=self.count+1
    def DeQueue(self):
        if self.count==0:
            return -1
        self.arr.pop(0)
        self.count=self.count-1

    def Front(self):
        if self.count==0:
            return -1
        return self.arr[self.front]
    def Size(self):
        return self.count
    def isEmpty(self):
        return self.count==0



q=QueueUsingArray()
print(q.isEmpty())
q.EnQueue(1)
q.EnQueue(2)
q.EnQueue(3)
print(q.isEmpty())
print(q.Front())
print(q.Size())
q.DeQueue()
q.DeQueue()
q.DeQueue()
print(q.isEmpty())
print(q.Front())
print(q.Size())


