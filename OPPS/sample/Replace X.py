def replaceChar(s):
    if len(s)==0:
        return s
    Hypo=replaceChar(s[1:])
    if s[0]=="x":
        return Hypo
    else:
        return s[0]+Hypo
print(replaceChar("xaxb"))
