class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
printLL(node2)