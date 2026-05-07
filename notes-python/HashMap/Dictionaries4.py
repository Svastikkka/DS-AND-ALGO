"""
d1={}
s=input("first dict").split()
for i in s:
    if i  in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1
print(d1)

"""

d1={}
s=input("first dict").split()
k=2 #frequency
for i in s:
    d1[i]=d1.get(i,0)+1
for i in d1:
    if d1[i]==k:
        print(i)