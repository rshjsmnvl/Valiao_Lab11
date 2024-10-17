print("Welcome to GPA Calculator!")
# Enter the name and section of the user
name = str(input("Name: "))
section = str(input("Section: "))
# Get the user's period grades
prelims = float(input("Enter your Preliminary Period Grade: "))
midterm = float(input("Enter your Midterm Period Grade: "))
finals = float(input("Enter your Final Period Grade: "))
final_grade = round((prelims*0.3333)+(midterm*0.3333)+(finals*0.3333))
print("Final Grade: " + str(final_grade))
# Output error
if prelims <= 40:
    print("Error: Enter a valid grade for Preliminary Period.")
if midterm <= 40:
    print("Error: Enter a valid grade for Midterm Period.")
if finals <= 40:
    print("Error: Enter a valid grade for Final Period.")
# Calculate GPA
if final_grade <= 100 and final_grade >= 99:
    print("Your Final Grade is 1.00")
elif final_grade <= 98 and final_grade >= 96:
    print("Your Final Grade is 1.25")
elif final_grade <= 95 and final_grade >= 93:
    print("Your Final Grade is 1.50")
elif final_grade <= 92 and final_grade >= 90:
    print("Your Final Grade is 1.75")
elif final_grade <= 89 and final_grade >= 87:
    print("Your Final Grade is 2.00")
elif final_grade <= 86 and final_grade >= 84:
    print("Your Final Grade is 2.25")
elif final_grade <= 83 and final_grade >= 81:
    print("Your Final Grade is 2.50")
elif final_grade <= 80 and final_grade >= 78:
    print("Your Final Grade is 2.75")
elif final_grade <= 77 and final_grade >= 75:
    print("Your Final Grade is 3.00")
elif final_grade < 75:
    print("Your Final Grade is 5.0")
else:
    print("Invalid Input")