class genericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()



def inputTree():
    data=int(input())
    if data is -1:
        return None
    #create a node
    root=genericTreeNode(data)

    print(f"Enter a number of children for {root.data}")
    num=int(input())
    for i in range(num):
        child=inputTree()
        root.children.append(child)
    return root



def printTree(root):
    if root is None:
        return None
    print(root.data,end=":")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree(child)


printTree(inputTree())
