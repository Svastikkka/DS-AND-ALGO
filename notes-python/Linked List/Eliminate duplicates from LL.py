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
            NewNode=Node(i)
            if head is None:
                head=NewNode
                tail=NewNode
            else:
                tail.next=NewNode
                tail=NewNode
    return head
def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head=head.next

# This function removes duplicates from list
def removeDuplicates(head):
        temp = head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return head

t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    printLL(removeDuplicates(LinkedList(arr)))
