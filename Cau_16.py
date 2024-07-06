from math import *
import random

def check_prime(n):
    if n < 2 : return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True

def sinhMang(n):
    mang=[]

    for i in range(n):
        mang.append(random.randint(1,100))
    return mang

def timNguyenTo(mang):
    prime =[]
    for i in mang :
        if check_prime(i):
            prime.append(i)
    return prime
if __name__ == '__main__':
    n = int(input("Nhap so luong can sinh :"))
    mang = sinhMang(n)
    print(mang)
    print("Cac so nguyen to trong mang :",timNguyenTo(mang))





