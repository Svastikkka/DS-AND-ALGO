def BinarySearch(a,si,ei,x):
    if si > ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        ei=mid-1
        return BinarySearch(a,si,ei,x)
    elif a[mid]<x:
        si=mid+1

        return BinarySearch(a,si,ei,x)

l=[1,2,3,4,5,6,7]
print(BinarySearch(l,0,6,5))