from math import *
def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return True
def nguyenToSinhDoi(n):
    for i in range (1,n + 1):
        for j in range (1,n + 1):
            if check(i) and check(j) and abs(i-j) == 2:
                return i,j
if __name__ == '__main__':
    n = int(input())
    print(nguyenToSinhDoi(n))