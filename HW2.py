# HW2
# Nested for loop
rows = 3
columns = 4

#Create a 2D matrix (list of lists)
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

#Constant multiplier for the mathematical operation
multiplier = int(input("Enter the multiplier: ")) ## prompt the user in the console for this number (test it with a small number like 2)

# Multiply each element in the matrix by the multiplier
for i in range(rows):
    for j in range(columns):
        matrix[i][j] *= multiplier

# Output the updated matrix
print("Updated Matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
