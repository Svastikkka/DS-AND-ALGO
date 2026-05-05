## n to 1
def print_n_to_0(n):
    if n==0:
        return
    print(n)
    return  print_n_to_0(n-1)


## 1 to n
def print_0_to_n(n):
    if n==0:
        return 0
    print_0_to_n(n-1)
    print(n)

print(print_n_to_0(5))
print(print_0_to_n(5))