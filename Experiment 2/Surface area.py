'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''

print("Enter details for surface area calculations:")

side = float(input("Enter the side length of the cube: "))
cube_surface_area = 6 * (side ** 2)

cuboid_length = float(input("Enter the length of the cuboid: "))
cuboid_width = float(input("Enter the width of the cuboid: "))
cuboid_height = float(input("Enter the height of the cuboid: "))
cuboid_surface_area = 2 * ((cuboid_length * cuboid_width) + (cuboid_width * cuboid_height) + (cuboid_length * cuboid_height))

print("\n==============================")
print("        SURFACE AREA RESULTS")
print("==============================")
print(f"Cube Surface Area   : {cube_surface_area}")
print(f"Cuboid Surface Area : {cuboid_surface_area}")
print("==============================\n")

