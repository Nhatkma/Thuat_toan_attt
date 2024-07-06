from math import *

def uocChung (a,b):
    while b > 0 :
        tmp = a % b
        a = b
        b = tmp
    return a
def check(n):
    if n < 2 : return False
    for i in range(2, isqrt(n) +1 ):
        if n % i == 0:return False
    return True

def cnt(mang):
    cnt = 0
    n = len(mang)
    for i in range(n):
        for j in range(i +1 , n):
            if check(uocChung(mang[i], mang[j])):
                cnt += 1
    return cnt

if __name__ == "__main__":
    mang = list(map(int, input("Nhap mang :").split()))
    print("So cap (i,j)sao cho uoc chung lớn nhất là số nguyen tố",cnt(mang))
