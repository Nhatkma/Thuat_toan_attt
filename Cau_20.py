from math import *

def uoc(a,b):
    while ( b > 0):
        tmp = a % b
        a = b
        b = tmp
    return a
def tim (m,n,d):
    for i in range(m,n):
        for j in range(m,n):
            if uoc(i,j) == d:
                print(i,j )
if __name__ == '__main__':
    M, N, P = map(int, input().split())
    tim(M,N,P)



