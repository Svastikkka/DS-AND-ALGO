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
    return root

def NodeAtDepth(root,k=0):
    if root is None:
        return
    if k==0:
        print(root.data,end=" ")
        return
    NodeAtDepth(root.left,k-1)
    NodeAtDepth(root.right,k-1)

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
#preOrder(inputTree())
NodeAtDepth(inputTree(),1)