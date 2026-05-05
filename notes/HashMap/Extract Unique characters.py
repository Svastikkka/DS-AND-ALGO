class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Map:
    def __init__(self):
        self.bucketSize=5
        self.bucket=[None for i in range(self.bucketSize)]
        self.count=0

    def getValue(self,key):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None


    def getBucketIndex(self,hc):
        return (abs(hc)%self.bucketSize)


    def insert(self,key,value):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                return
            head=head.next
        head=self.bucket[index]
        NewNode=MapNode(key,value)
        NewNode.next=head
        self.bucket[index]=NewNode
        self.count+=1


    def rehash(self):
        temp=self.bucket
        self.bucket=[None for i in range(self.bucketSize*2)]
        self.bucketSize=(self.bucketSize*2)
        self.count=0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head=head.next


    def getUnique(self,s):
        arr=[]
        temp = self.bucket
        for head in temp:
            while head is not None:
                arr.append(head.value)
                head = head.next
        for i in s:
            if i  in arr:
                print(i,end="")
                arr.remove(i)
m=Map()
s=list(map(str,input().strip()))
for i in s:
    m.insert(i,i)
m.getUnique(s)