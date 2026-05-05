#REVERSE LINKED LIST USING RECURRSION IT TAKES O(N^2)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def LinkedList(arr):
    head=None
    tail=None
    if len(arr)<1:
        return None
    else:
        for i in arr:
            if i==-1:
                break
            else:
                NewNode=Node(i)
                if head is None:
                    head=NewNode
                    tail=NewNode
                else:
                    tail.next=NewNode
                    tail=NewNode
    return head
def printLL(head):
    while head is not  None:
        print(head.data,end=" ")
        head=head.next
    print()



def reverseLL(head):

    if head is None or head.next is None:
        return head
    smallHead=reverseLL(head.next)
    current=smallHead

    while current.next is not None:
        current=current.next

    current.next=head
    head.next=None

    return smallHead

arr=list(map(int,input().split()))
printLL(reverseLL(LinkedList(arr)))

