class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height(root):
    if root is None:
        return 0
    leftNode=height(root.left)
    rightNode=height(root.right)
    return 1+max(leftNode,rightNode)


def inputTree():
    data=int(input())
    if data is -1:
        return
    root=BinaryTreeNode(data)
    root.left=inputTree()
    root.right=inputTree()
    return root

def preOrder(root):
    if root is None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print(root.left.data,end=",")
    if root.right is not  None:
        print(root.right.data,end="")
    print()
    preOrder(root.left)
    preOrder(root.right)
print(height(inputTree()))
#preOrder(inputTree())


