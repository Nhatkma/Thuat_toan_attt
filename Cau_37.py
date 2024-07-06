from math import *
def tienXuLi(p,m,lps):
    len=0
    i=1
    lps[0]=0
    while i<m:
        if p[i]==p[len]:
            lps[i]=len+1
            len+=1
            i+=1
        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1
def kmp(p,t):
    n=len(t)
    m=len(p)
    lps=[0]*m
    tienXuLi(p,m,lps)
    i=0
    j=0
    while i<n:
        if t[i]==p[j]:
            i+=1
            j+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
        if j==m:
            print('chỉ số bắt đầu:',i-j)
            j=lps[j-1]
if __name__ =='__main_':
    t= input("Nhap van ban :")
    p=  input("Nhap van ban tim kiem :")
    kmp(p,t)