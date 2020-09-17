"Implementation of stack using list "

arr=[]
def BalancedParanthesis(str):
    for i in str:
        if i in "{[(":
            arr.append(i)
        if i is ")":
            if len(arr)<1 or arr[-1]!="(":
                return False
            arr.pop()
        if i is "}":
            if len(arr)<1 or arr[-1]!="{":
                return False
            arr.pop()
        if i is i is "]":
            if len(arr)<1 or arr[-1]!="[":
                return False
            arr.pop()

    if len(arr)==0:
        return True

    return False







str = input()
if BalancedParanthesis(str):
    print("true")
else:
    print("false")



