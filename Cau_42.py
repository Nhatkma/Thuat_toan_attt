from math import *
import random

def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n) + 1 ):
        if n % i == 0:
            return False
    return True
def sinhSoNguyenTo():
    while True:
        num = random.randint(1,1000)
        if check(num):
            return num

def nbpcl(a):
    k = sinhSoNguyenTo()
    n = sinhSoNguyenTo()
    b = 1
    if k == 0 : return b
    A = a
    mang = []
    while k > 0 :
        mang.append(k % 2 )
        k //=2
    if mang[0] == 1:
        b = A
    for i in range(1,len(mang)):
        A = A * A % n
        if mang[i] == 1:
            b = A * b % n
    return b

def inRa(a):
    for i in range(1, a + 1):
        if check(nbpcl(i)):
            print(i,end =" ")

if __name__ == "__main__":
    a= int(input("Nhap a:"))
    inRa(a)