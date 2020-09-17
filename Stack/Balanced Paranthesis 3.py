"Implementation of stack using linked list "
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def PushLL(self,arr):
        NewNode=Node(arr)
        NewNode.next=self.head
        self.head=NewNode
        self.size=self.size+1

    def PopLL(self):
        self.head=self.head.next
        self.size=self.size-1


def BalancedParanthesis(str):
    ll=LinkedList()
    for i in str:
        if i in "{[(":
            ll.PushLL(i)
        if i is ")":
            if ll.size==0 or ll.head.data!="(":

                return False
            ll.PopLL()
        if i is "}":
            if ll.size==0 or ll.head.data!="{":
                return False
            ll.PopLL()
        if i is i is "]":
            if ll.size==0 or ll.head.data!="[":
                return False
            ll.PopLL()

    if ll.size==0:
        return True

    return False

ele=input()
if BalancedParanthesis(ele):
    print("true")
else:
    print("false")








