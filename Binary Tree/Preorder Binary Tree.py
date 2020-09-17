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
def preOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)


def postOrder(root):

    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")

preOrder(inputTree())
postOrder(inputTree())


