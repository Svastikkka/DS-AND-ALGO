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

def MergeSortedLL(head1,head2):


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

def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print(None)

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

printLL(MergeSortedLL(LinkedLists(arr1),LinkedLists(arr2)))
