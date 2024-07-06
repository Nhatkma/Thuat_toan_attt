from math import *
import random
def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n) + 1 ):
        if n % i == 0:
            return False
    return True
def sinh(n):
    while True:
        p = random.randint(1,n)
        if check(p):
            return p
def nbpcl(a,n):
    k = sinh(n)
    b = 0
    A =a
    mang = []
    while k > 0 :
        mang.append(k % 2)
        k //= 2
    if mang[0] == 1:b = A
    for i in range(1,len(mang)):
        A = A * A % n
        if mang[i] == 1 :
            b = A * b % n
    return b

def inRa(a,n):
    for i in range(1,n+1):
        if check(nbpcl(a,i)):
            print(i)

if __name__ == "__main__":
    a = int(input("Nhap a :"))
    n = int(input("Nhap n :"))
    print(inRa(a,n))