class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def LinkedLists(arr):
    head=None
    tail=None
    for i in arr:
        if len(arr)==0:
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

def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print(None)

arr = list(map(int, input().split()))
printLL(LinkedLists(arr))
