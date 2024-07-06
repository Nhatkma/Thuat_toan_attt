from math import *
def check (n):
    if n < 2 :return False
    for i in range (2,isqrt(n) + 1 ):
        if n % i == 0:
            return False
    return True
def kiemTra(l,r):
    tong = 0
    for i in range (l,r):
        tong +=i
        if check(tong):
            return True
    return False
if __name__ == '__main__' :
    l,r = map(int,input().split())
    if kiemTra(l,r):
        print("YES")
    else :
        print("NO")