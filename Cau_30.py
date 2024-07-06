from math import *

def check_prime(n):
    if n < 2 :return False
    for i in range (2,isqrt(n) + 1):
        if n % i == 0:return False
    return True

def uocChung(a,b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def nbpcl(a,k,n):
    b =1
    mang=[]
    A = a
    if k == 0 : return b
    while k > 0 :
        mang.append(k % 2)
        k //= 2
    if mang[0] == 1 :
        b = A
    for i in range(1,len(mang)):
        A = A * A % n
        if mang[i] == 1 :
            b = A * b % n
    return b

def isCarmichael(n):
    if n < 2 or check_prime(n):
        return False
    for b in range ( 1 , n ):
        if uocChung(b,n) == 1 :
            if nbpcl(b,n-1,n) != 1 :
                return False
    return True

def tong(n):
    tong= 0
    for i in range(1,n+1):
        if isCarmichael(i):
            tong+=i
    return tong


if __name__ == '__main__':
    n = int(input("Nhap n :"))
    print(f"Tong cua cac so carmicharl be hon N = {tong(n)} " )