from math import *
import random

def nbpcl(a,k,n):
    b = 1
    A = a
    mang =[]
    if k == 0 :
        return b
    while k > 0 :
        mang.append(a % 2)
        k //= 2

    if mang[0] == 1 : b = A
    for i in range(1,len(mang)):
        A = A * A % n
        if mang[i] == 1 :
            b = A * b % n
    return b
def check(n):
    if n < 2 : return False
    for i in range (2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def sinh ():

    while True:
        a = random.randint(100, 500)
        if check(a):
           return a
def uocChung(a,b):
    while b > 0 :
        tmp = a % b
        a = b
        b = tmp
    return a

def nghichDao(a,b):
    if b == 0:
        return a, 1, 0
    x2, x1, y2, y1 = 1, 0, 0, 1

    while b > 0:
        q = a // b
        r = a - q * b
        x, y = x2 - q * x1, y2 - q * y1

        a, b = b, r
        x2, x1, y2, y1 = x1, x, y1, y

    return a, x2, y2
def mod(a,p):
    uoc,x,y = nghichDao(a,p)
    if uoc != 1 :
        return False
    else: return x % p

def rsa(m):
    p = sinh()
    q = sinh()
    n = p*q
    pi = (p-1)*(q-1)
    e = random.randint(1,pi)
    while uocChung(pi,e)!= 1:
        e = random.randint(1, pi)
    d =mod(e,n)
    c = nbpcl(m + 123,e,n)
    m = nbpcl(c,d,n)
    print(f"Số nguyên tố p: {p}")
    print(f"Số nguyên tố q: {q}")
    print(f"n = p * q: {n}")
    print(f"pi = (p - 1) * (q - 1): {pi}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"ban max c cua thong diep m la :{c}")
    print(f"Giai ma thong diep =",m)


if __name__ == '__main__':
    SBD = int(input("SBD: "))
    rsa(SBD)