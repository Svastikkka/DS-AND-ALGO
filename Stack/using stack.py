
from Stack.stack import Stack

obj=Stack()
obj.push(1)
obj.push(2)
while obj.isEmpty() is False:
    print(obj.pops())