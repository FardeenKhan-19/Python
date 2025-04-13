'''
Fardeen Khan
UIN : 241P096 / Roll no : 27
FE Computer Engineering
Div : D
'''
print("Student Enrollment Management System")

cet_students = {"Alice", "Bob", "Charlie", "David"}
jee_students = {"Charlie", "David", "Eve", "Frank"}
neet_students = {"Alice", "Eve", "George", "Helen"}

print("\nEnrolled Students:")
print(f"CET Students: {cet_students}")
print(f"JEE Students: {jee_students}")
print(f"NEET Students: {neet_students}")

union_all = cet_students | jee_students | neet_students
intersection_cet_jee = cet_students & jee_students
difference_cet_neet = cet_students - neet_students

print("\n==============================")
print("          SET OPERATIONS")
print("==============================")
print(f"All Unique Students Enrolled (Union): {union_all}")
print(f"Students Enrolled in Both CET & JEE (Intersection): {intersection_cet_jee}")
print(f"Students Enrolled in CET but Not in NEET (Difference): {difference_cet_neet}")
print("==============================\n")
