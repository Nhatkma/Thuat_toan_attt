def last_occurrence(p):
    tienXuLi = {}
    for i in range(len(p)):
        tienXuLi[p[i].lower()] = i
    return tienXuLi

def find_p(t, p, l):

    n = len(t)
    m = len(p)
    i = m - 1
    lap = 0

    while i < n:
        j = m - 1
        matched = True
        while j >= 0 and matched:
            if t[i].lower() == p[j].lower():
                i -= 1
                j -= 1
            else:
                matched = False
            lap += 1  #TANG KHI SO SANH DUOC
        if j < 0:
            return i + 1, lap
        else:
            bad_char = t[i].lower()
            i += m - min(j, 1 + l.get(bad_char, -1))

    return -1, lap

def boyer_moore(t, p):
    t = t.lower()
    p = p.lower()

    if len(p) > len(t):
        print("Mẫu cần tìm kiếm dài hơn văn bản")
        return

    l = last_occurrence(p)
    vitri, lap = find_p(t, p, l)
    if vitri != -1:
        print(f"'{p}' có trong '{t}' bắt đầu tại vị trí {vitri}")
    else:
        print(f"'{p}' không có trong '{t}' ")
    print(f"Số lần lặp: {lap}")

if __name__ == "__main__":
    T = input("Nhập văn bản: ")
    P = input("Nhập mẫu cần tìm kiếm: ")
    boyer_moore(T, P)
