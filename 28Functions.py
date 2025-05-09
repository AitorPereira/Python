def greeting():
    print ("Good morning")

greeting()

def greeting(name):
    print ("Good Morning " + name)

name = "Antonio"
greeting(name)

def add(num1,num2):
    sum = num1 + num2
    return sum

num1=7
num2=10

result = add(num1,num2)
print (result)

#Pass By Reference
colors = ["green","red","blue"]

def add_color(colors,color):
    colors.append(color)

color = "black"
add_color(colors,color)

print (colors)