#Input for size of matrix1
x1, y1 = raw_input().split()
#Convert to int values
x1, y1 = [int(x1), int(y1)]
#Add required number of ints for list
var1 = x1*y1

#-->>add while loop adding all inputs into matrix1
matrix = [i[:] for i in [[0]*x1]*y1]

##################

#Input for size of matrix2
x2, y2 = raw_input().split()
#Convert to int values
x2, y2 = [int(x2), int(y2)]
#Add required number of ints for list
var2 = x2*y2

#-->>add while loop adding all inputs into matrix2
matrix2= [j[:] for j in [[0]*x2]*y2]

##################

#Show contents of matrices
print(matrix)
print(matrix2)
