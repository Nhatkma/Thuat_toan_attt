from math import *

def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def uoc(a,b):
    while b > 0 :
        tmp = a % b
        a = b
        b = tmp
    return a

def uocChungNguyenTo(n):
    for i in range(1, n ):
        for j in range(i ,n ):
            if check(uoc(i,j)):
                print(f"{i},{j}")

if __name__ == '__main__':
    n = int(input("Nhap n :"))
    uocChungNguyenTo(n)