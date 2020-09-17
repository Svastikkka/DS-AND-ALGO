"""Figure out the largest node in the tree"""


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inputTree():
    data=int(input())
    if data is -1:
        return
    root=BinaryTreeNode(data)
    root.left=inputTree()
    root.right=inputTree()
    return  root

def largetData(root):
    if root is None:
        return -1
    leftNode=largetData(root.left)
    rightNode=largetData(root.right)
    return max(leftNode,rightNode,root.data)



def preOrder(root):
    if root is None:
        return -1
    print(root.data,end=" ")
    if root.left is not None:
        print(root.left.data,end=",")
    if root.right is not None:
        print(root.right.data,end="")
    print()
    preOrder(root.left)
    preOrder(root.right)

#preOrder(inputTree())
print(largetData(inputTree()))



