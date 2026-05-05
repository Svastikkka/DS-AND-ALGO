class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def Enqueue(self,data):
        NewNode=Node(data)
        if self.head == None:
            self.head=NewNode
            self.tail=NewNode
            self.count=self.count+1
        else:
            self.tail.next=NewNode ##giving address of new newnode
            self.tail=NewNode  ##assign a new node
            self.count=self.count+1

    def DeQueue(self):
        if self.count ==0:
            return -1
        data=self.head.data
        self.head=self.head.next
        self.count = self.count - 1
        return data

    def Front(self):
        return self.head.data
    def size(self):
        return self.count

    def isEmpty(self):
        return self.count==0

    def printLL(self):
        while self.head is not None:
            print(self.head.data,end=" ")
            self.head=self.head.next
        print()

l=LinkedList()
l.Enqueue(1)
l.Enqueue(2)
l.Enqueue(3)
print(l.Front())
print(l.size())
print(l.isEmpty())
print(l.DeQueue())
l.printLL()

