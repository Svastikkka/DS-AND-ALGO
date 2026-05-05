import queue


def reverseFirstK(q, k):
    if (q.empty() == True or
            k > q.qsize()):
        return
    if (k <= 0):
        return

    Stack = []

    # put the first K elements
    # into a Stack
    for i in range(k):
        Stack.append(q.queue[0])
        q.get()

        # Enqueue the contents of stack
    # at the back of the queue
    while (len(Stack) != 0):
        q.put(Stack[-1])
        Stack.pop()

        # Remove the remaining elements and
    # enqueue them at the end of the Queue
    for i in range(q.qsize() - k):
        q.put(q.queue[0])
        q.get()


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
    q.put(ele)
k = int(input())
reverseFirstK(q, k)
while (q.qsize() > 0):
    print(q.get())
    n -= 1