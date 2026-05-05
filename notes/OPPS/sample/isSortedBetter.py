"""
Updation of isSorted
"""
def isSorted(arr,si):
    l=len(arr)
    if si ==l-1 or si == l:
        return True
    if arr[si] >arr[si+1]:
        return False
    return isSorted(arr,si+1)


arr=[1,6,2,3,4,5]
print(isSorted(arr,0))