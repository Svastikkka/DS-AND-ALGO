class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Map:
    def __init__(self):
        self.bucketSize=10
        self.bucket=[None for i in range(self.bucketSize)]
        self.count=0

    def size(self):
        return self.count


    def getValue(self,key):
        hc=hash(key)
        index=self.bucketIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                return (head.value)
            head=head.next
        return None

    def deleteValue(self,key):
        hc=hash(key)
        index=self.bucketIndex(hc)
        head=self.bucket[index]
        prev = None

        while head is not None:
            if head.key==key:
                if prev is None:
                    self.bucket[index]=head.next
                else:
                    prev.next=head.next
                self.count-=1
                return head.value
            prev=head
            head=head.next
        return None


    def bucketIndex(self,hc):
        return (abs(hc)%self.bucketSize)

    def insert(self,key,value):
        hc=hash(key)
        index=self.bucketIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return

            head=head.next
        head=self.bucket[index]
        NewNode=MapNode(key,value)
        NewNode.next=head
        self.bucket[index]=NewNode
        self.count+=1

m=Map()
#getsize of list
m.insert("manshu",2)
print(m.size())
m.insert("manshu",21)
print(m.size())
m.insert("mother",45)
print(m.size())

#get Value of key
print("----",m.getValue("manshu"))
print(m.getValue("anshu"))

#delete Value from a linkedlist
print(m.deleteValue("manshu"))
print(m.deleteValue("anshu"))



