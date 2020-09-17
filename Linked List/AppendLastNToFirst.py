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


def appendLastNToFirst(head, k):
    h0 = head
    total = 0
    while (h0 is not None):
        h0 = h0.next
        total += 1
    if total<k:
        return None
    current = head
    count = 1
    while (count < total - k  and current is not None):
        current = current.next
        count += 1
    NewNode = current
    while (current.next is not None):
        current = current.next
    current.next = head  #head --> None
    head = NewNode.next #head --- NewNode
    NewNode.next = None
    printLL(head)


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    n = int(input())
    appendLastNToFirst(LinkedLists(arr), n)