"""Taking level wise input """

import queue




class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelWiseInput():
    data=int(input())
    if data is -1:
        return
    root=BinaryTreeNode(data)
    q = queue.Queue()
    q.put(root)
    while  not q.empty():
        current_node=q.get()
        print("Enter a left child for",current_node.data)
        leftChildData=int(input())
        if leftChildData is not -1:
            leftNode=BinaryTreeNode(leftChildData)
            current_node.left=leftNode
            q.put(leftNode)
        print("Enter a right child for",current_node.data)
        rightChildData=int(input())
        if rightChildData is not -1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root
def printLevelWise(root):
    if root is None:
        return
    q1=queue.Queue()
    q1.put(root)
    while not q1.empty():
        current_node=q1.get()
        print(current_node.data,end=":")
        if  current_node.left is not None:
            print("L:",end="")
            print(current_node.left.data,end=",")
            q1.put(current_node.left)
        else:
            print("L:-1",end=",")
        if current_node.right is not None:
            print("R:",end="")
            print(current_node.right.data,end="")
            q1.put(current_node.right)
        else:
            print("R:-1",end="")
        print()


printLevelWise(levelWiseInput())



