from math import *

def nbpcl(a,k,n):
    b = 1
    if k == 0 : return b
    A =a
    mang =[]
    while k > 0:
        mang.append(k % 2)
        k //= 2
    if mang[0] == 1 :
        b =a

    for i in range (1,len(mang)):
         A = A * A % n
         if mang [i] == 1 :
             b = (A * b ) % n
    return b

if __name__ == '__main__':
    a,k,n = map(int,input().split())
    print(nbpcl(a,k,n))