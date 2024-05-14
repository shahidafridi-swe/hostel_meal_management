            
array = [[0 for _ in range(7)] for _ in range(31)]

# Set the first column values to 1 through 31
for i in range(31):
    array[i][0] = i + 1

# Print the array to verify
for row in array:
    print(row)