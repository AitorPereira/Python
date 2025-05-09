# Create a variable "grade1" with the value 6
# Create another variable "grade2" with the value 4
# Create another variable "grade3" with the value 7
# Create another variable "average_grades" with the average value of the 3 previous grades
# Create another variable "final_grades" with the value "passed" (if the average is greater than or equal to 5)

grade1 = 6
grade2 = 4
grade3 = 7
average_grades = (grade1 + grade2 + grade3) / 3
final_grades = "passed"

if average_grades >= 5:
    print (final_grades)
else:
    print ("F")