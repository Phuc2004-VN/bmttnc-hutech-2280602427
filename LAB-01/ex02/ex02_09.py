def kt_snt(n):
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False
    return True

number = int(input("Nhập vào số cần kiểm tra: "))
if kt_snt(number):
    print(number, "Là số nguyên tố.")
else:
    print(number,"Không phải số nguyên tố.")