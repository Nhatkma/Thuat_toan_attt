from math import *
import random

def nbpcl(a,k,n):
    b = 1
    A = a
    mang = []
    if k ==0 : return b
    while k > 0 :
        mang.append(k % 2 )
        k //= 2

    if mang[0] == 1: b = A
    for i in range(1,len(mang)):
        A = A *A % n
        if mang[i] == 1:
            b = A * b % n
    return b

def miller_Rabin(n):
    if n < 2 : return False
    s = 0
    r = n -1
    while r % 2 == 0 :
        s +=1
        r //= 2
    for i in range(5):
        a = random.randint(2,n-2)
        y = nbpcl(a,r,n)
        if y !=1 and y != n -1 :
            j = 1
            while j <= s -1 and y != n - 1 :
                y = y * y % n
                if y == 1 :
                    return False
                j +=1
            if y != n - 1:
                return False
    return True
def timSoNguyenToGanNhat(n):
    if miller_Rabin(n)  :
        return n

    lower = n -1
    upper = n +1
    while True:
        if lower > 1 and miller_Rabin(lower) :
            return lower
        if miller_Rabin(upper):
            return upper

        lower -= 1
        upper += 1

if __name__ == '__main__':
    n = int(input("Nhap n > 0:"))
    print(f"So Nguyen to gan nhat :{timSoNguyenToGanNhat(n)}")
    SBD = int(input("SBD:"))
    k = nbpcl(SBD,timSoNguyenToGanNhat(n),123456)
    print(k)