# Exercise

# Create the function "primes" which will be a generator function 
# that yields prime numbers between 0 and 100

# This is the list of prime numbers between 0 and 100
#prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
#                 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Use the generator function to display on screen the prime numbers less than 50

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

#We could do even numbers like these:

#def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False

def prime():
    for number in range (0,101):
        if is_prime(number):
            yield number

print ("These are the prime numbers below 100: {}".format(list(prime())))

list_below_50 = []
for n in prime():
    if n < 51:
        list_below_50.append(n)
print ("These are prime numbers below 50: {}".format(list_below_50))



#Now, if the number_list is given, this is how we proceed:

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def is_prime2(max):
    for n in range(max):
        if n in prime_numbers:
            yield n
        if (n > 100):
            break

max = 50
for num in is_prime2(max):
    print (num)