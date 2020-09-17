import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    if root is None:
        return
    q1=queue.Queue()
    q1.put(root)
    while not q1.empty():
        current_node=q1.get()
        print(current_node.data,end=":")
        if  current_node.left is not None:
            print("L:",end="")
            print(current_node.left.data,end=",")
            q1.put(current_node.left)
        else:
            print("L:-1",end=",")
        if current_node.right is not None:
            print("R:",end="")
            print(current_node.right.data,end="")
            q1.put(current_node.right)
        else:
            print("R:-1",end="")
        print()



def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelWise(root)
