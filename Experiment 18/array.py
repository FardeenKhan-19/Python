'''
Fardeen Khan
UIN: 241P096 / Roll no: 27
FE Computer Engineering
Div: D
'''
import numpy as np

print("1D Array")
one_d_array = np.array([1, 2, 3, 4, 5])
print("Original 1D Array:", one_d_array)

print("\nIndexing 1D Array (Element at index 2):", one_d_array[2])
print("Slicing 1D Array (Elements from index 1 to 3):", one_d_array[1:4])

reshape_2d = one_d_array.reshape(1, 5)
print("Reshaped 1D to 2D (1x5):", reshape_2d)

print("\n2D Array")
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D Array:")
print(two_d_array)

print("\nElement at (0, 2) in 2D array:", two_d_array[0, 2])
print("First row of the 2D array:", two_d_array[0])
print("Elements from row 1, columns 1 to 2:", two_d_array[1, 1:3])

reshape_3d = two_d_array.reshape(1, 2, 3)
print("Reshaped 2D to 3D (1x2x3):")
print(reshape_3d)

print("\n3D Array")
three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Original 3D Array:")
print(three_d_array)

print("Element at (1, 0, 2) in 3D array:", three_d_array[0, 1, 2])
 