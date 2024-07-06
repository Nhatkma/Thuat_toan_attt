from math import *
def check(n):
    if n < 2 : return False
    for i in range(2 ,isqrt(n) + 1 ):
        if n % i == 0: return False
    return True
def duaRSoNguyenTo(n):
    mang = []
    for i in range (2 , n + 1) :
        if check(i):
            mang.append(i)
    return mang
def timKiem(M,N,mang):
    def deQuy(batDau,demSoTrongMangKiemTra,tongHienTai,mangKiemTra):
        if demSoTrongMangKiemTra == M :
            if tongHienTai == N :
                return mangKiemTra
            return None
        if batDau >= len(mang) or tongHienTai > N :
            return None
        for i in range(batDau,len(mang)):
            mangKiemTra.append(mang[i])
            kq = deQuy(i + 1,demSoTrongMangKiemTra + 1, tongHienTai + mang[i],mangKiemTra )
            if kq:
                return kq
            mangKiemTra.pop()
        return None
    return deQuy(0,0,0,[])

if __name__ == '__main__':
    N = int(input("Nhap N:"))
    M = int(input("Nhap M:"))
    mang = duaRSoNguyenTo(N)
    kq = timKiem(M,N,mang)
    if kq :
        print(f"{N} Phân tích thành tổng của  {M} số nguyên  tố {kq}")
    else :
        print(f"{N} không phân tích được thành {M} số nguyên tố")