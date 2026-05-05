def maxFreq(l):
    # Please add your code here
    # creating a dictionary
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    # creating a dictionary
    size=0
    key=None
    for i in d:
        if d[i]>size:
            size=d[i]
            key=i
    return key


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
