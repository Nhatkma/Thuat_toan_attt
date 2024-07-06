from math import *
def check(n):
    if n < 2 :
        return False
    for i in range(2,isqrt(n) + 1 ):
        if n % i == 0 :
            return False
    return True
def nbpcl(a,k,n):
    b =1
    if k == 0 : return b
    mang =[]
    A = a
    while k > 0 :
        mang.append(k % 2)
        k //= 2
    if mang[0] == 1:
        b = A
    for i in range(1,len(mang)):
        A = A * A % n
        if mang[i] == 1:
            b = A *b % n

    return b

if __name__ == "__main__":
    a,k,n = map(int,input("Nhap a,k,n :").split())
    if check(nbpcl(a,k,n)):
        print("Yes")
    else:
        print("No")

    print(nbpcl(a,k,n))