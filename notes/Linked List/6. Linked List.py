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
            NewNode = Node(i)
            if head==None:
                head=NewNode
                tail=NewNode
            else:
                tail.next=NewNode
                tail=NewNode
    return head


def insertAtPosition(i,head,data):
    count=0
    previous = None
    current = head
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


def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print(None)

arr=list(map(int,input().split()))
printLL(LinkedLists(arr))
printLL(insertAtPosition(5,LinkedLists(arr),6))
