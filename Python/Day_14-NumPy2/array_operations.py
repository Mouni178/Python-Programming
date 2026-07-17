import numpy as np
# Creating Arrays
arr = np.array([10,20,30,40,50,60])
print("Original Array")
print(arr)
# Indexing
print("\nFirst Element")
print(arr[0])
print("\nThird Element")
print(arr[2])
print("\nLast Element")
print(arr[-1])
# Slicing
print("\nSlicing")
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::-1])
# Updating Elements
print("\nUpdating")
arr[3] = 100
print(arr)
# Reshape
print("\nReshape")
arr2 = np.array([1,2,3,4,5,6])
print(arr2.reshape(2,3))
print(arr2.reshape(3,2))
# Flatten
print("\nFlatten")
matrix = np.array([[1,2],[3,4]])
print(matrix.flatten())
