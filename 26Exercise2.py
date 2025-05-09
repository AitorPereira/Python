#Create a variable "grade" with the value 4.5  
#Create a variable "work_done" with the value "yes"  
#Calculate the value of the variable "final_grade", considering that if the grade is greater than or equal to 4,
#and the value of the variable "work_done" is equal to "yes", then "final_grade" will be equal to "passed";
#otherwise, it will be equal to "failed"

grade = 3
work_done = "yes"
final_grade = ""

if (grade>=4) and (work_done == "yes"):
    final_grade = "passed"
    print (final_grade)
else:
    final_grade = "failed"
    print (final_grade)