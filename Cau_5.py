from math import *

import random

def nbpcl(a,k,n):
    b = 1
    A = a
    mang = []
    if k == 0 : return b

    while k > 0:
        mang.append(k % 2)
        k //= 2

    if mang[0] == 1 :
        b = A

    for i in range(1,len(mang)):
        A = A * A % n
        if mang[i] == 1 :
            b = A * b % n
    return b

def check(n):
    s = 0
    r = n - 1
    while r % 2 == 0 :
        s += 1
        r //= 2

    for i in range(3):
        a = random.randint(2,n - 2)
        y = nbpcl(a,r,n)

        if y != 1 and y != n -1 :
            j =1
            while j < s - 1 and y != n - 1 :
                y = y * y % n

                if y == 1:
                    return False

                j += 1
            if y != n -1 :
                return False
    return True
def tongSoNguyenTo (a,b):
    tong = 0
    for i in range(a,b):
        if check(i):
            tong+=i
    return tong
if __name__== '__main__':
    a,b = map(int,input("Nhap khoang a va b :").split())
    print(tongSoNguyenTo(a,b))