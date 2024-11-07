passed_count = 0
all_grades = []
i = 1
x = 0

grade = input(f"Enter Grade of Student {i} and type 'done' to finish: ")

while grade.lower() != "done":
    if float(grade) >= 40 and float(grade) <= 100:
        all_grades.append(float(grade))
        if float(grade) >= 75:
            passed_count += 1
    else:
        print("Error: Invalid Grade. Enter a valid grade between 40 and 100")
        x += 1
        break
    i += 1
    grade = input(f"Enter Grade of Student {i} and type 'done' to finish: ")

average = sum(all_grades) / len(all_grades)
pass_percent = (passed_count / len(all_grades)) * 100
print(f"Entered Grades: {all_grades}")
print(f"Averaged Grades: {average: .2f}")
print(f"No. of Students Passed: {passed_count} students passed.")
print(f"Passing %: {pass_percent}%")