class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def TakeInput():
    l=[int(i) for i in input().split()]
    head=None
    tail=None
    for i in l:
        if i==-1:
            break
        data = Node(i)
        if head is None:
            head=data
            tail=data
        else:
            tail.next=data
            tail=data
    return head


def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head = head.next
    print(None)



printLL(TakeInput())
