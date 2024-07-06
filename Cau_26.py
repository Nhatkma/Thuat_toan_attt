from math import *
def check (n):
    if n < 2 :return False
    for i in range (2,isqrt(n) + 1 ):
        if n % i == 0:
            return False
    return True
def soManhMe(n):
    for i in range(1,n):
        if check( n // i ) and check( n // i * i):
            print(i)
if __name__ == '__main__' :
    n = int(input())
    soManhMe(n)
