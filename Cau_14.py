from math import *
def check(n):
    if n < 2 : return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return True
def lapPhuong(n):
    rot = round(n // 3)
    return rot * 3 == n
def inRa():
    #start = 10 **(n-1)
    #end = 10 ** n
    for i in range(100,10000):
        if check(i) :
            re = int(str(i)[::-1])
            if lapPhuong(re) :
                return re

if __name__ == '__main__':

    print(inRa())
