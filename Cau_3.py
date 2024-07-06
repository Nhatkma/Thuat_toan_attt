from math import *
import random

def check(n):
    if n < 2 :
        return False
    for i in range(2 , isqrt(n) +1 ):
        if n % i == 0:
            return False
    return True

def uocNguyenTo(n):
    cnt = 0
    for i in range(1 , n):
        if check(i) and n % i == 0:
            cnt += 1

    return cnt
def tongUocNguyenTo(n):
    tong = 0
    for i in range(1 , n +1 ):
        if check(i) and n % i == 0:
            tong += i
    return tong
def uoc(n):
    cnt = 0
    for i in range( 1 , n+1):
        if n % i == 0 :
            cnt += 1

    return cnt

def tongUoc(n):
    tong= 0
    for i in range( 1 , n + 1):
        if n % i == 0:
            tong += i
    return tong
if __name__ == "__main__":
     n = int(input("Nhap n :"))
     k =uocNguyenTo(n)
     q = tongUocNguyenTo(n)
     p =tongUoc(n)
     s = uoc(n)
     print(n + p + s - q - k)