from math import *
import random

def nbpcl(a, k, n):
    b = 1
    A = a
    if k == 0:
        return b
    while k > 0:
        if k % 2 == 1:
            b = (b * A) % n
        A = (A * A) % n
        k //= 2
    return b
def kiem_tra_miller_rabin(n, t):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n < 2:
        return False
    r = n - 1
    s = 0
    while r % 2 == 0:
        s += 1
        r //= 2
    for _ in range(t):
        a = random.randint(2, n - 2)
        y = nbpcl(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j < s and y != n - 1:
                y = (y * y) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True


def sinh_mang_nguyen_to(n, t):
    mang = []
    so = 2
    while len(mang) < n:
        if kiem_tra_miller_rabin(so, t):
            mang.append(so)
        so += 1
    return mang

def khoang_cach_nho_nhat(mang):
    if len(mang) < 2:
        return 0
    mang.sort()
    kcnn = float('inf')
    for i in range(len(mang) - 1):
        khoang_cach = abs(mang[i] - mang[i + 1])
        kcnn = min(khoang_cach,kcnn)
    return kcnn

if __name__ == '__main__':
    t = int(input("Nhập t: "))
    n = int(input("Nhập n > 2: "))
    mang_nguyen_to = sinh_mang_nguyen_to(n, t)
    print("Mảng các số nguyên tố:", mang_nguyen_to)
    print("Khoảng cách nhỏ nhất giữa 2 số trong mảng:", khoang_cach_nho_nhat(mang_nguyen_to))
