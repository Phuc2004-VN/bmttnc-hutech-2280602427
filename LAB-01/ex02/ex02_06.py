input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(' ')]
rowNum = dimensions[0]
colNum = dimensions[1]
mutilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        mutilist[row][col] = row * col

for i in range(0, len(mutilist)-1):
    print(mutilist[i], end="\n")
print(mutilist[len(mutilist)-1])