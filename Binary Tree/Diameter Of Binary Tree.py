class  BinaryTreeNode:
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
    return root

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

def diameter(root):
    if root is None:
        return 0

    option1 =height(root.left)+height(root.right)
    option2=diameter(root.left)
    option3=diameter(root.right)
    return max(option1,option2,option3)


def preOrder(root):
    if root is None:
        return
    print(root,end=" ")
    if root.left is not None:
        print(root.left.data,end=",")
    if root.right is not None:
        print(root.right.data,end="")
    print()
    preOrder(root.left)
    preOrder(root.right)

print(diameter(inputTree()))
