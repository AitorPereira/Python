#Docstrings - strings to generate documentation

def greeting(name):
    """
    This is a comment for the greeting function.
    This function receives a string with a name as a parameter
    and prints a greeting with the name concatenated.
    """
    print ("Good morning " + name)

greeting("Antonio")

#help (greeting)

class Greets:
    """
    This class will have two functions: good morning and goodbye
    Both functions receives a name as a parameter
    """
    def good_morning(self, name):
        """
        This function is used to say good morning to somebody
        """
        print("Good morning {}!".format(name))
    
    def goodbye(self,name):
        """
        This function is used to say goodbye to somebody
        """
        print("Goodbye {}".format(name))

greet = Greets()
greet.good_morning("John")

help(Greets)

#every time we want to use how to use a function we can use help() for example help(len)