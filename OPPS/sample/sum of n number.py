def sum_of_n_num(n):
    if n==1:
        return 1
    return sum_of_n_num(n-1)+n
num = int(input())
print(sum_of_n_num(num))