from math import *

def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n) + 1):
        if n % i == 0: return False
    return True

def binhPhuong(x,y):
    return x *x + y *y
def timKiem(a,b,s1,s2):
    cnt = 0
    mang=[]
    for i in range( a, b +1 ):
        if check(i):
            mang.append(i)

    for x in s1 :
       for y in s2 :
          kq = binhPhuong(x,y)
          if kq in mang:
              cnt += 1
    return cnt
if __name__ == '__main__':
    a,b = map(int, input("Nhap a , b :").split())
    s1 = [1,2,3]
    s2 = [3,4,6]
    print(f"so luong so nguuyen to trong khoang [{a},{b}] là tổng của hai số s1 và s2 : {timKiem(a,b,s1,s2)}")
