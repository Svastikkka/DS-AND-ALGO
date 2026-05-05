def reverseStack(arr1, arr2):
    if len(arr1)<=1:
        return
    if len(arr1)!=1:
        ele1=arr1.pop()
        arr2.append(ele1)
    lastElement=arr1.pop()

    while len(arr2) !=0:
        ele=arr2.pop()
        arr1.append(ele)
    reverseStack(arr1,arr2)
    arr1.append(lastElement)

from sys import  setrecursionlimit
setrecursionlimit(11000)
arr1=list(map(int,input().split()))
arr2=[]
reverseStack(arr1,arr2)
while len(arr1)!=0:
    print(arr1.pop(),end=" ")