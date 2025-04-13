'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''

print("Enter details for area calculations:")

radius = float(input("Enter the radius of the circle: "))

circle_area = 3.14 * radius * radius

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle_area = length * width

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

triangle_area = 0.5 * base * height


print("\n==============================")
print("        AREA RESULTS")
print("==============================")
print(f"Circle Area    : {circle_area}")
print(f"Rectangle Area : {rectangle_area}")
print(f"Triangle Area  : {triangle_area}")
print("==============================\n")