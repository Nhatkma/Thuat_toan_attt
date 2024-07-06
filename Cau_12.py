from math import *
def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return True

def timSo(n):
    cnt = 0
    mang = []
    for i in range(1,n+1):
        if check(i):
            cnt += 1
            mang.append(i)
            if cnt == 4:
                break
    return mang
if __name__ == '__main__':
    n = int(input())
    print(f"Bon so nguyen lien tiep :{timSo(n)}")