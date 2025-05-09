#While

value = 1
end = 10

#while (value < end):
#    print(value)
#    value = value + 1

#Break is use to get out of the loop
while (value < end):
    print(value)
    value = value + 1
    if (value == 5):
        break

#Continue is use to skip a number in this case
while (value < end):
    print(value)
    value = value + 1
    if (value == 5):
        continue
    print (value)