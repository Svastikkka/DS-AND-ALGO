import queue
q=queue.LifoQueue()
def checkRedundant(string):
    flag=False
    for i in string:
        if i is ")":
            if q.empty() or q.queue[-1]!="(":
                flag=False
            q.get()

    if q.empty():
        return True
    return False



string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')




