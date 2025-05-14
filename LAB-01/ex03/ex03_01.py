def tong_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cách nhay khoảng trắng: ")
numbers = list(map(int, input_list.split(' ')))

tongchan = tong_chan(numbers)
print("Tồng các số chẵn trong List là: ", tongchan)


