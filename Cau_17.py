from math import *
def check (n):
    if n < 2 :return False
    for i in range (2,isqrt(n)):
        if n % i == 0:
            return False
    return True
def timKiem(a,b,c,n):
    for x in range(1,n):
        y = a * ( x ** 2) + b * x +c
        if check(y):
            return x
    return -1


if __name__ == '__main__' :
    a,b,c ,n= map(int,input().split())
    x = timKiem(a,b,c,n)
    if x == -1 :
        print("khong co")
    else :
        print(f"x :{x}" )