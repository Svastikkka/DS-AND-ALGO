#STACK
arr=list(map(int,input().split()))

#push
arr.append(int(input()))
#pop
arr.pop()


#QUEUES
import queue

q=queue.Queue()
q.put(1)
q.put(1)
q.put(1)
q.put(1)
q.put(1)

while not q.empty():
    print(q.get())



