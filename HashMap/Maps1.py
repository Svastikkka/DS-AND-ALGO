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


    def getBucketIndex(self,hc):
        return (abs(hc)%self.bucketSize)

    def insert(self,key,value):
        hc =hash(key)
        index=self.getBucketIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        newNode=MapNode(key,value)
        newNode.next=head
        self.bucket[index]=newNode
        self.count+=1


m=Map()
m.insert("manshu",2)
m.insert("manshu",2)
print("1",m.size())
m.insert("manshu",21)
print("2",m.size())
m.insert("mother",45)
print(m.size())


