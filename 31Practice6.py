# Create a class named 'Movie' that has a constructor (__init__ method)
# which receives 3 parameters: 'title', 'director', and 'year'.
# These values are stored in attributes with the same names as the parameters.

class Movie:
    def __init__(self,title,director,year):
        self.title = title
        self.director = director
        self.year = year
        