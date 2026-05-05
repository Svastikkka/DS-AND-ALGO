def replaceChar(s):
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    Hypo = replaceChar(s[1:])
    if s[0] == "p" and s[1]=="i":
        return Hypo
    else:
        return s[0:1] + Hypo



# Main
string = input()
print(replaceChar(string))