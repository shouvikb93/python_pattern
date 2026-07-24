#students name, marks in a dictionary

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[name] = marks

search = input("Enter student name: ")

marks = students.get(search)

if marks is not None:
    print(search, "scored", marks)
else:
    print("Student not found.")