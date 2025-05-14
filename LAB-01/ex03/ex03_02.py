def daonguoc_list(chuoi):
    return chuoi[::-1]

input_list = input("Mời nhập danh sách cần đảo ngược: ")
numbers = list(map(int, input_list.split(' ')))

list_dao = daonguoc_list(numbers)

for i in range(0, len(list_dao)-1):
    print(list_dao[i], end="")
print("Chuỗi đảo ngược là: ",list_dao[len(list_dao)-1])