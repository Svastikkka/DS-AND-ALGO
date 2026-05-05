class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
def inputLL(arr):
    head = None
    tail = None
    if len(arr)==0:
        return None
    for i in arr:
        if i is -1:
            break
        NewNode=LinkedListNode(i)
        if head is None:
            head=NewNode
            tail=NewNode
        else:
            tail.next=NewNode
            tail=NewNode
    return head
def FindNode(count,head,data):
    if head is None:
        return None

    if head.data==data:
        return count
    return FindNode(count+1,head.next,data)

def printLL(head):
    if head is  None:
        return None
    while head is not  None:
        print(head.data,end=" ")
        head=head.next
t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    n=int(input())
    if FindNode(0,inputLL(arr),n) is not None:
        print(FindNode(0,inputLL(arr),n))
    else:
        print(-1)


