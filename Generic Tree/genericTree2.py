class genericTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()


root=genericTreeNode(5)
node1=genericTreeNode(2)
node2=genericTreeNode(9)
node3=genericTreeNode(8)
node4=genericTreeNode(7)
node5=genericTreeNode(15)
node6=genericTreeNode(1)

root.children.append(node1)
root.children.append(node2)
root.children.append(node3)
root.children.append(node4)

node2.children.append(node5)
node2.children.append(node6)


## using simple preorder use for binary tree give not good traversing but traverse every node
def printTree(root):
    # it is not a base case it is a edge case if root is None then it simply return None and not go to root.data
    # but if we remove this edge case it simply may  gives error at point root.data because None not has any data
    if root is None:
        return None
    print(root.data)
    for child in root.children:
        printTree(child)
printTree(root)
print()
print()

## using simple preorder with some changes which gives good traversing and traverse every node
def printTreeDetailed(root):
    # it is not a base case it is a edge case
    if root is None:
        return None
    print(root.data,end=":")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTreeDetailed(child)


printTreeDetailed(root)