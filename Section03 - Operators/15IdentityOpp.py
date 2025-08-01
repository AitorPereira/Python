#Identity Operators (is, is not)

fruits1 = ["apple", "orange", "banana"]
fruits2 = ["apple", "orange", "banana"]
fruits3 = fruits1

if fruits3 is fruits1:
    print("true")

fruits3.append("kiwi")
print (fruits3)
print (fruits1)

if fruits3 is not fruits2:
    print("False")