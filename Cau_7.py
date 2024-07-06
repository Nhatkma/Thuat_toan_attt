from math import *

def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n)):
        if n % i == 0 :
            return False
    return  True
def emirp(n):

    for i in range(10,n+1):
        if check(i):
            re = int(str(i)[::-1])
            if check(re):
                print(re, end = " ")


if __name__ == '__main__' :
    n = int(input())
    emirp(n)