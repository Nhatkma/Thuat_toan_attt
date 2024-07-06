from math import *

import random

def nbpcl(a,k,n):
    b = 1
    A = a
    mang = []
    if k == 0 : return b

    while k > 0:
        mang.append(k % 2)
        k //= 2

    if mang[0] == 1 :
        b = A

    for i in range(1,len(mang)):
        A = A * A % n
        if mang[i] == 1 :
            b = A * b % n
    return b

def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n) +1 ):
        if n % i == 0:
            return False
    return True

def dem (a,b):
    cnt = 0
    for i in range(a,b):
        if check(i):
            cnt += 1
    return cnt

if __name__== '__main__':
    a,b = map(int,input("Nhap khoang a va b : ").split())
    print(dem(a,b))