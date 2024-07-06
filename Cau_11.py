from math import *
def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return True

def tong(n):
    tong = 0
    for i in range(1,n+1):
        if check(i):
            print(i)
            tong += i
    return tong
if __name__ == '__main__':
    n = int(input())
    print(tong(n))