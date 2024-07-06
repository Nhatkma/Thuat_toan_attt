from math import *
def dieuKien(n):
    cnt = 0
    for i in range(1,n):
        if n % i == 0:
            cnt+=1
            if cnt > 4:
                return False
    return cnt ==4
def inCacSo(n):
    for i in range(1,n+1):
        if dieuKien(i):
            print(i , end = " ")
if __name__ == '__main__':
    n = int (input())
    inCacSo(n)
