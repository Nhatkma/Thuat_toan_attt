from math import *
def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return True

def two_prime(n):
    if n < 5 :return None
    for i in range(1,n+1):
        if check(i + 2) and check(abs(i -2)):
            return 2,i
    return None
if __name__ == '__main__':
    n = int(input())
    print(two_prime(n))