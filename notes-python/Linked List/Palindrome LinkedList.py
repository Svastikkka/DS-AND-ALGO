class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def LinkedList(arr):
    head=None
    tail=None
    if len(arr)<1:
        return
    else:
        for i in arr:
            if i ==-1:
                break
            NewNode = Node(i)
            if head == None:
                head=NewNode
                tail=NewNode
            else:
                tail.next=NewNode
                tail=NewNode
    return head

def printLL(head):
    arr=[]
    while head is not None:
        arr.append(head.data)
        head=head.next
    if arr[0:]==arr[::-1]:
        print('true')
    else:
        print('false')
t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    printLL(LinkedList(arr))