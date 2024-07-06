def uocChung(a,b):
    while b > 0 :
        tmp = a % b
        a = b
        b =tmp
    return a
def nghichDao(p,mang):
    mangB =[]
    for i in range(len(mang)):
        a,b = p , mang[i]
        x2, x1, y2, y1 = 1, 0, 0, 1
        while b > 0:
           q = a // b
           r = a - q * b
           x, y = x2 - q * x1, y2 - q * y1

           a, b = b, r
           x2, x1, y2, y1 = x1, x, y1, y
        if y2< 0:
           y2 += p
        mangB.append(y2)
    return mangB

if __name__ == '__main__':
    p = int(input("Nhap p : "))
    mang= list(map(int, input("Nhap mang :").split()))
    mangB = nghichDao(p,mang)
    print("Mang nghich dao :",mangB)


