from math import *
def check (n):
    if n < 2 :return False
    for i in range (2,isqrt(n)):
        if n % i == 0:
            return False
    return True
def tim(a,b,c,m,l):
    for x in range(m,l+1):
        y = a * (x**2) + b * x + c
        if check(y):
            print(x)

if __name__ == '__main__' :
    a,b,c,m,l = map(int,input().split())
    print(tim(a,b,c,m,l))
