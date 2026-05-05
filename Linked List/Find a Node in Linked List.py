class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def LinkedLists(arr):
    head=None
    tail=None
    if len(arr)<1:
        return -1
    else:
        for i in arr:
            if i is not -1:
                NewNode=Node(i)
                if head is None:
                    head=NewNode
                    tail=NewNode
                else:
                    tail.next=NewNode
                    tail=NewNode
            else:
                break
    return head
def printLL(head,n):
    arr=[]
    while head is not None:
        arr.append(head.data)
        head=head.next
    if arr.__contains__(n):
        print(arr.index(n))
    else:
        print(-1)

for i in range(int(input())):
    arr=list(map(int,input().split()))
    n=int(input())
    printLL(LinkedLists(arr),n)
