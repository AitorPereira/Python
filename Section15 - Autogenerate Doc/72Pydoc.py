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

#Go to my terminal on Mac, access to the folder by using cd and ls
#Once im in use: pydoc + .py file name to obtain all comments in my terminal
#In case I want to obtain a HTML file with all instructions and comments write on my terminal:
#pydoc -w and the route to the file for example: pydoc -w /Users/Documents/Python/Section15/Pydoc.py