j=[]
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print("Các số từ 2000 đến 3200 chia hết cho 7 mà không phải bội của 5 gồm: ")
for i in range(0, len(j)-1):
    print(j[i], end=", ")
print(j[len(j)-1])