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

def removeLeafNode(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return None

    root.left=removeLeafNode(root.left)
    root.right=removeLeafNode(root.right)


    return root


def preOrder(root):
    if root is None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print(root.left.data,end=",")
    if root.right is not None:
        print(root.right.data,end="")
    print()
    preOrder(root.left)
    preOrder(root.right)

preOrder(removeLeafNode(inputTree()))
