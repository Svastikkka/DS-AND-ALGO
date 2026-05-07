class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
def inputLL(arr):
    if len(arr)==None:
        return None
    head=None
    tail=None
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

def middleLL(head):
    if head is None:
        return None
    fast=head
    slow=head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow
def mergeLL(head1,head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    mergedHead = None
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next
    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead


def sortLL(h):
    # Base case if head is None
    if h == None or h.next == None:
        return h

    middle = middleLL(h)
    nexttomiddle = middle.next
    middle.next = None
    left = sortLL(h)
    right = sortLL(nexttomiddle)
    sortedlist = mergeLL(left, right)
    return sortedlist


def printLL(head):
    if head is None:
        return None
    while head is not None:
        print(head.data,end=" ")
        head=head.next

n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    printLL(sortLL(inputLL(arr)))