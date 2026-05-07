"""Try to improve it """
def reverseStack(arr1,arr2):
    if len(arr1)<0:
        return
    while len(arr1)!=0:
        ele= arr1.pop()
        arr2.append(ele)
    while len(arr2)!=0:
        ele= arr2.pop()
        arr1.append(ele)




arr1=list(map(int,input().split()))
arr2=[]
reverseStack(arr1,arr2)
while len(arr1)!=0:
    print(arr1.pop(),end=" ")

