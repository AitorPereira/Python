name = "Aitor"
print ("My name is " + name)

#format
name = "Aitor"
age = 30
print ("Good morning {}, happy {} birthday". format(name,age))

result = 10 / 3
print (result)

#A way to concatenate a variable with a string
print("The result is: {r}".format(r=result))

#We use "1.3f" to declare we want only 3 decimals
print("The result is: {r:1.3f}".format(r=result))

#f-string

name = "Aitor"
age = 30
print (f"Good morning {name}, happy {age} birthday")