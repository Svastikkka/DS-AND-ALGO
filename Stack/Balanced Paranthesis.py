"Implementation of stack using built in queue "

import queue
q=queue.LifoQueue()

def isBalanced(str):
    for i in str:
        if i is "[" or i is "{" or i is "(":
            q.put(i)
        if i is "]":
            if q.empty() or q.queue[-1]!="[":
                return False
            q.get()
        if i is ")":
            if q.empty() or q.queue[-1]!="(":
                return False
            q.get()
        if i is i is "}":
            if q.empty() or q.queue[-1]!="{":
                return False
            q.get()

    if q.empty():
        return True

    return False
expression=input()
if isBalanced(expression):
    print("true")
else:
    print("false")