from math import *


def check(n):
    if n < 2 : return False
    for i in range(2 , isqrt(n) +1 ):
        if n % i == 0:return False
    return True
def nbpcl(a,k,n):
    b = 1
    A = a
    mang = []
    if k == 0 :
        return b
    while k > 0:
        mang.append(k % 2)
        k //= 2
    if mang[0] == 1 :b =A
    for i in range(1,len(mang)):
        A = (A * A) % n
        if mang[i] == 1:
            b = (A * b) % n
    return b
def uocChung(a,b):
    while b > 0 :
        tmp = a % b
        a= b
        b = tmp
    return a
def isCarmichael(n):
    if n < 2 or check(n):
        return False
    for b in range(2,n):
        if uocChung(b,n) == 1:
            if nbpcl(b,n-1,n)!=1 :
                return False
    return True

def carmichael(n):
    mang =[]
    for i in range(2,n):
        if isCarmichael(i):
            mang.append(i)
    return mang
if __name__ == '__main__':
    n = int(input("nhap n :"))
    print("Các số Carmichael nhỏ hơn N là :",carmichael(n))