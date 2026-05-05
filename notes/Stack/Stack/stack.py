class Stack:
    def __init__(self):
        self.__arr=[] #CLASS VARIABLE

    def push(self,n):
        return self.__arr.append(n)

    def getpush(self):
        return self.__arr
    def setpush(self,n):
        self.__arr.append(n)

    def pops(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        else:
            return self.__arr.pop()
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.__arr[-1]
    def isEmpty(self):
        return len(self.__arr)==0


