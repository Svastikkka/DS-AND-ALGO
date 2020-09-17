class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+self.b


arr1=[4,5]
arr2=[6,7]


p=complex(arr1,arr2)
print(p.__add__(arr1))


