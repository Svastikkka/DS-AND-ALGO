class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def LinkedLists(arr):
    head=None
    tail=None
    for i in arr:
        if i==-1:
            break
        else:
            NewNode=Node(i)
            if head==None:
                head=NewNode
                tail=NewNode
            else:
                tail.next=NewNode
                tail=NewNode
    return head

def printLL(index,head):
    c=0
    while head is not None:
        if c==index:
            return head.data
        head=head.next
        c=c+1

for i in range(int(input())):
    arr = list(map(int, input().split()))
    index=int(input())
    if len(arr)>=index and arr.index(-1)>index:
        print(printLL(index,LinkedLists(arr)))
    else:
        print()
