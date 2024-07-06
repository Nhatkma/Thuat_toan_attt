def nghichDao(a,b):
    if b == 0:
        return a, 1, 0
    x2, x1, y2, y1 = 1, 0, 0, 1

    while b > 0:
        q = a // b
        r = a - q * b
        x, y = x2 - q * x1, y2 - q * y1

        a, b = b, r
        x2, x1, y2, y1 = x1, x, y1, y

    return a, x2, y2
def mod(a,p):
    uoc,x,y = nghichDao(a,p)
    if uoc != 1 :
        return False
    else: return x % p
if __name__ == '__main__':
    a, p= map(int, input("Nhap a va p :").split())
    if mod(a,p) :
        print(f"nghich dao cua {a} trong trường Fp là :",mod(a,p))
    else :
        print(f"{a} khong co nghịch dao trong truong fp")