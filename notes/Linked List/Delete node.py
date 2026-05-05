class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def LinkedLists(arr):
    head=None
    tail=None
    if len(arr)<1:
        return
    else:
        for i in arr:
            NewNode=Node(i)
            if head is None:
                head=NewNode
                tail=NewNode
            else:
                tail.next=NewNode
                tail=NewNode
    return head

def insertAtPosition(head,i,data):
    count=0
    previous=None
    current=head
    while count<i:
        previous=current
        current=current.next
        count=count+1
    NewNode=Node(data)
    if previous is not None:
        previous.next=NewNode
    else:
        head=NewNode
    NewNode.next=current
    return head

def deleteAtPosition(head,i,data):
    pass

def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print(None)


arr=list(map(int,input().split()))
printLL(LinkedLists(arr))
position=int(input())
printLL(insertAtPosition(LinkedLists(arr),position,6))
