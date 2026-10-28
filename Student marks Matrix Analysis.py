students = ["Arun", "Banu", "Charan"]

marks = [
    [85, 90, 78],
    [92, 88, 95],
    [76, 80, 84]
]

totals = []

print("STUDENT MARKS ANALYSIS")
print("-" * 40)

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(marks[i])
    totals.append(total)

    print("Student:", students[i])
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))
    print()

print("SUBJECT-WISE AVERAGES")

for j in range(len(marks[0])):
    subject_total = 0

    for i in range(len(students)):
        subject_total += marks[i][j]

    subject_average = subject_total / len(students)
    print("Subject", j + 1, ":", round(subject_average, 2))

top_index = totals.index(max(totals))

print("\nTop Performer:", students[top_index])
print("Highest Total:", totals[top_index])
