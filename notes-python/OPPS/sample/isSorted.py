def isSorted(n):
    size=len(n)
    if size<=1:
        return True
    if n[0]>n[1]:
        return False
    SmallList =isSorted(n[1:])
    if SmallList :
        return True
    else:return False
arr=[1,7,3,4,5,6]
print(isSorted(arr))
