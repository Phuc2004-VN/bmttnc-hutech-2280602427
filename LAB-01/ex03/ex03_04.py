def phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Nhập tuple, vd (1, 2, 3): "))
first, last = phan_tu(input_tuple)

print("Phần tử đầu: ", first)
print("Phần tử cuối: ", last)