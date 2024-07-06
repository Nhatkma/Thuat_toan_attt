from math import *

def dieuKien(n):
    cnt = 0
    if n <= 2 : return False
    for i in range(3,n+1):
        if n % i == 0:
            cnt += 1
            if cnt > 3 :
                return False
    return cnt == 3

def inRa(n):
    for i in range(1,n+1):
        if dieuKien(i):
            print(i,end=" ")



if __name__ == '__main__':
    n = int (input())
    inRa(n)