from math import *

def check(n):
    if n < 2 :return False
    for i in range(2 ,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def quyUoc(n):
    if check(n):
        return n
    else:
        return 0
def tong(l,r):
    tong = 0
    for i in range(l,r+1):
        for j in range(l,r+1):
            if j > i :
               tong += quyUoc(i) * quyUoc(j)
    return tong
if __name__ == '__main__':
    l,r = map(int,input("Nhap l,r :").split())
    print(tong(l,r))