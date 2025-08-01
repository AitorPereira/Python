#Series

import pandas as pd

#This will create an index list
serie1 = pd.Series([3,5,7])
print (serie1) # This will obtain: 0    3
                                   #1    5
                                   #2    7
                                   #dtype: int64

#If we need to access to any of these elements, we search by index position
print (serie1[1]) # This will obtain: 5


#To assign grades to the subject list we will have to define a variable as a pd.series type and pass grades and as index
#the subject names
subject = ['history','math','literature','science','economics']
grades = [9,4,3,5,7]

serie_thomas_grades = pd.Series (grades, index=subject)
print (serie_thomas_grades)

#To select grades from a single subject
print (serie_thomas_grades['math'])

#To select all subjects over 8
print (serie_thomas_grades[serie_thomas_grades >= 8])

#To name a list
serie_thomas_grades.name = 'Thomas grades list'
print (serie_thomas_grades)

#To name an index
serie_thomas_grades.index.name = 'Thomas subjects'
print (serie_thomas_grades)

#To convert a list into a dictionary
diccionary = serie_thomas_grades.to_dict()
print (diccionary)

#To convert a diccionary to a list
serie = pd.Series(diccionary)
print (serie)


subject = ['history','math','literature','science','economics']
grades = [6,5,9,4,8]
serie_daniel_grades = pd.Series(grades, index=subject)
print(serie_daniel_grades)

#To average grades

serie_grades_class = (serie_thomas_grades + serie_daniel_grades) / 2
print (serie_grades_class)
