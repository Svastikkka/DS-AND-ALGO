class genericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

def inputTree():
    data=int(input())
    if data is -1:
        return
    root=genericTreeNode(data)
    print(f"Enter a number of children {root.data}")
    num=int(input())
    for child in range(num):
        child=inputTree()
        root.children.append(child)
    return root


def numNode(root):
    if root is None:
        return 0
    count=1
    for child in root.children:
        count=count+numNode(child)
    return count


def printTree(root):
    if root is None:
        return None
    print(root.data,end=":")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree(child)

print(numNode(inputTree()))