def even_num(n):
    if n==2:
        print(2)
        return
    elif n%2==0:
        even_num(n-1)
        print(n)

    else:
        even_num(n-1)
print(even_num(100))
