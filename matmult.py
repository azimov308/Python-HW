'''
Matrix1
'''
#Input for size of matrix1
try:
    x1, y1 = raw_input().split()
except:
    pass
#Convert to int values
x1, y1 = [int(x1), int(y1)]

matrix1 = []
count1 = x1

while count1 != 0:
    new_list = [float(val) for val in raw_input().split()]
    if len(new_list) != y1:
        #print("Too many/few inputs!")
        exit()
    matrix1.append(new_list)
    count1 = count1 - 1

#print(matrix1)


'''
Matrix2
'''
#Input for size of matrix1
x2, y2 = raw_input().split()
#Convert to int values
x2, y2 = [int(x2), int(y2)]
#Testcase to see if you can multiply
if y1 != x2:
    print("invalid input")
    exit()

matrix2 = []
count2 = x2

while count2 != 0:
    new_list2 = [float(val) for val in raw_input().split()]
    if len(new_list2) != y2:
        #print("Too many/few inputs!")
        exit()
    matrix2.append(new_list2)
    count2 = count2 - 1

#print(matrix2)


'''
Matrix multiplication
'''
r=[]
m=[]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        sums=0
        for k in range(len(matrix2)):
            sums=sums+(matrix1[i][k]*matrix2[k][j])
        r.append(sums)
    m.append(r)
    r=[]
print(m)
