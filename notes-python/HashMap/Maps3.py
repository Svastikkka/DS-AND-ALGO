class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Map:
    def __init__(self):
        self.bucketSize=5
        self.bucket=[None for i in  range(self.bucketSize)]
        self.count=0
    def size(self):
        return self.count

    def getBucketIndex(self,hc):
        return (abs(hc)%self.bucketSize)

    def insert(self,key,value):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        head=self.bucket[index]
        newNode=MapNode(key,value)
        newNode.next=head
        self.bucket[index]=newNode
        self.count+=1
        loadFactor=self.count/self.bucketSize
        if loadFactor>=0.7:
            self.rehash()
    def getValue(self,key):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None


    def loadFactor(self):
        return self.count/self.bucketSize


    def rehash(self):
        temp=self.bucket
        self.bucket=[None for i in range(self.bucketSize*2)]
        self.bucketSize=(self.bucketSize*2)
        self.count=0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head=head.next


m=Map()
for i in range(17):
    m.insert("abc"+str(i),i)
    print(m.loadFactor() ,  "abc"+str(i) , m.getValue("abc"+str(i)))

