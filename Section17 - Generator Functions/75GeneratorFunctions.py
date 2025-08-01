range (0,11)

for num in range (0,11):
    print (num)

range (11)

#This range (0,11) and this range (11) is the same


def odds (max):
    for num in range(max):
        if (num % 2 == 0):
            yield num

max = 11
for num in odds(max):
    print(num)