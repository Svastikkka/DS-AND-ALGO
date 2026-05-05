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


