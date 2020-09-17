class BinarTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inputTree():
    data=int(input())
    if data is -1:
        return
    root=BinarTreeNode(data)
    root.left=inputTree()
    root.right=inputTree()
    return root

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))
def isBalanced(root):
    if root is None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if lh-rh>1or rh-lh>1:
        return False
    isLeftBalanced=isBalanced(root.left)
    isRightBalanced=isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

def isBalanced2(root):
    if root is None:
        return 0,True
    lh,isLeftBalanced=isBalanced2(root.left)
    rh,isRightBalanced=isBalanced2(root.right)
    h=1+max(lh,rh)
    if lh-rh>1 or rh-lh>1:
        return h,False
    if isLeftBalanced or isRightBalanced:
        return h,True
    else:
        return h,False


def preOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    if root.left is not None:
        print(root.left.data,end=",")
    if root.right is not None:
        print(root.right.data,end="")
    print()
    preOrder(root.left)
    preOrder(root.right)

#preOrder(inputTree())
#print(height(inputTree()))
print(isBalanced2(inputTree()))