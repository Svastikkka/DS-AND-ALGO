#REVERSE LINKED LIST USING RECURRSION IT TAKES O(N)
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
        return head,head
    smallHead,smallTail=reverseLL(head.next)
    smallTail.next=head
    head.next=None

    return smallHead,head

arr=list(map(int,input().split()))
head,tail=reverseLL(LinkedList(arr))
printLL(head)