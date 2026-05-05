"""
WORK ONLY FOR UNIQUE VALUES
"""
class LinkedListNode:
	def __init__(self,data):
		self.data=data
		self.next=None
def inputLL(arr):
	head=None
	tail=None
	if len(arr)==0:
		return None
	for i in arr:
		if i == -1:
			break
		NewNode=LinkedListNode(i)
		if head is None:
			head=NewNode
			tail=NewNode
		else:
			tail.next=NewNode
			tail=NewNode
	return head
def middleNodeLL(head):
	if head is None:
		return None
	fast=head
	slow=head
	while fast.next is not None and fast.next.next is not None:
		slow=slow.next
		fast=fast.next.next
	return slow
def printLL(head):
	if head is None:
		return None
	while head is not None:
		print(head.data,end=" ")
		head=head.next

n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    print(middleNodeLL(inputLL(arr)).data)
