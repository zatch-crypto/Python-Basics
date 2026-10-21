marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    average = sum(marks) / len(marks)

    print("Average marks =", average)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade =", grade)