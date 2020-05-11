n=int(input('Nhập số nguyên giai thừa cần tính: '))
def giaithua(n):
    if n==0 or n==1:
        return 1
    else:
        return n*giaithua(n-1)
print("kết quả số giai thừa là : ", giaithua(n))