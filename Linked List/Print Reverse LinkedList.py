class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def LinkedLists(arr):
    head = None
    tail = None
    if len(arr) < 1:
        return -1
    else:
        for i in arr:
            if i == -1:
                break
            NewNode = Node(i)
            if head == None:
                head = NewNode
                tail = NewNode
            else:
                tail.next = NewNode
                tail = NewNode
    return head


def printReverse(head) :
    prev = None
    current = head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    printLL(head)






def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next



arr = list(map(int, input().split()))
printReverse(LinkedLists(arr))