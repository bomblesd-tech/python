print("=== Student Data System ===")

name = input("Enter student name:")
roll_no = int(input("Enter roll number:"))
age = int(input("Enter age:"))
marks = float(input("Enter marks:"))

is_pass = marks >= 40

percentage = (marks / 100) * 100

print("\n=== Student Details ===")
print("Name:", name)
print("Roll Number:", roll_no)
print("Age:", age)
print("Marks:", marks)
print("Percentage:", percentage)
print("Result:", "Pass" if is_pass else "Fail")