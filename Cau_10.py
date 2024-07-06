from math import *
def check (n):
    if n < 2 : return False
    for i in range (2 , isqrt(n)+1):
        if n % i == 0 :
            return False
    return True

def dem(n):
    cnt_nt=0
    cnt=0
    for i in range (1,n + 1 ):
        if n % i == 0 :
            cnt += 1
            if check(i):
                cnt_nt+=1
    return cnt_nt,cnt

if __name__ == '__main__':
    n = int(input())
    print(dem(n))