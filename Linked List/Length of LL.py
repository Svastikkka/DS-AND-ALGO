class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def LinkedLists(arr):
    head=None
    tail=None
    for i in arr:
        if i== -1:
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
    count=0
    while head is not None:
        head=head.next
        count=count+1
    return count

for i in range(int(input())):
    arr = list(map(int, input().split()))
    print(printLL(LinkedLists(arr)))

