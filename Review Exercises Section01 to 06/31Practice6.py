# Create a class named 'Movie' that has a constructor (__init__ method)
# which receives 3 parameters: 'title', 'director', and 'year'.
# These values are stored in attributes with the same names as the parameters.

class Movie:
    def __init__(self,title,director,year):
        self.title = title
        self.director = director
        self.year = year
        
class1 = Movie("The Dark Knight","Christopher Nolan",2008)

print(class1.title)
print(class1.director)
print(class1.year)