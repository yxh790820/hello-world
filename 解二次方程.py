import math

def quadratic(a, b, c):
    x1 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1,x2
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
print(a,'x^2+',b,'x+',c,'=0的解为:','\n',quadratic(a, b, c))
input()