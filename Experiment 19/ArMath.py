'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
import numpy as np

# Function to take user input for an array
def input_array(name):
    rows = int(input(f"Enter the number of rows for {name}: "))
    cols = int(input(f"Enter the number of columns for {name}: "))
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Enter elements of row {i+1} separated by space: ").split()))
        elements.append(row)
    array = np.array(elements)
    print(f"\n{name}:\n", array)
    return array

# Input two arrays
array1 = input_array("Array 1")
array2 = input_array("Array 2")

# Ensure both arrays have the same shape
if array1.shape != array2.shape:
    print("Arrays must have the same shape for element-wise operations.")
else:
    # Element-wise operations
    addition = np.add(array1, array2)
    subtraction = np.subtract(array1, array2)
    multiplication = np.multiply(array1, array2)
    division = np.divide(array1, array2)

    # Display results
    print("\nElement-wise Addition:\n", addition)
    print("\nElement-wise Subtraction:\n", subtraction)
    print("\nElement-wise Multiplication:\n", multiplication)
    print("\nElement-wise Division:\n", division)

    # For dot and cross product, arrays must be 1D with 3 elements
    #if array1.ndim == 1 and array2.ndim == 1 and array1.size == 3 and array2.size == 3:
        # Dot product
    array3 = np.array([1, 2, 3])
    array4 = np.array([4, 5, 6])
    print("Array-3", array3)
    print("Array-4", array4)

    dot_product = np.dot(array3, array4)
    print("\nDot Product:", dot_product)

    # Cross product
    cross_product = np.cross(array3, array4)
    print("\nCross Product:", cross_product)