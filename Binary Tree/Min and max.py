"""
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 1567, Find the minimum and maximum value
def minMax(root):
    if root is None:
        return
    q1=queue.Queue()
    q1.put(root)
    INT_MAX=root.data
    INT_MIN=root.data
    while not q1.empty():
        current_node=q1.get()
        if current_node.left is not None:
            q1.put(current_node.left)
            if INT_MAX<current_node.left.data:
                INT_MAX=current_node.left.data
            if INT_MIN>current_node.left.data:
                INT_MIN=current_node.left.data
        if current_node.right is not None:
            q1.put(current_node.right)
            if INT_MAX<current_node.right.data:
                INT_MAX=current_node.right.data
            if INT_MIN>current_node.right.data:
                INT_MIN=current_node.right.data

    return INT_MIN,INT_MAX

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
minimum, maximum = minMax(root)
print(maximum, minimum)
"""


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 1567, Find the minimum and maximum value

def minimumData(root):
    if root== None:
        return INT_MAX
    res=root.data
    lres=minimumData(root.left)
    rres=minimumData(root.right)

    if lres<res:
        res=lres
    if rres<res:
        res=rres
    return res

def maximumData(root):
    if root == None:
        return INT_MIN
    res=root.data
    lres=maximumData(root.left)
    rres=maximumData(root.right)
    if lres>res:
        res=lres
    if rres>res:
        res=rres
    return res


def minMax(root):
    mini=minimumData(root)
    maxi=maximumData(root)

    return mini,maxi

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
minimum, maximum = minMax(root)
print(maximum, minimum)

