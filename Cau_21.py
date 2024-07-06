from math import *
def check (n):
    if n < 2 :return False
    for i in range (2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def sieuNguyenTo(l,r):
    cnt = 0
    cnt_1 = 0
    for i in range(l,r ):
        if check(i):
            cnt+=1
            if check(cnt):
                print(f"x = {i}",f"vi tri cua x:{cnt}")
                cnt_1+=1

    return cnt_1

if __name__ == '__main__' :
    l,r = map(int,input().split())
    print(sieuNguyenTo(l,r))

