def fact(n):
    if n==1:
        return 1
    return  2*fact(n - 1)+3
n=int(input('请输入项数:'))
print(fact(n))
input()