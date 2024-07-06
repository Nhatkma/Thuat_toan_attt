from math import *

def check(n):
    if n < 2 :
        return False
    for i in range(2 , isqrt(n)):
        if n % i == 0:
            return False
    return True
def dem (n):
    cnt = 0
    for i in range(n+1):
        if check(i):
            cnt += 1
    return cnt
if __name__== '__main__':
    n = int(input())
    print(dem(n))
