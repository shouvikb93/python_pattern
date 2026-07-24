#storing marks of student in a dictionary and then print that in terminal

students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter percentage marks: "))

    students[name] = marks

# print("Student Information")
# print("-------------------")

for name, marks in students.items():
    print(name, ":", marks)