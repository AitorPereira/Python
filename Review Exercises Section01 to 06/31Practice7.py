# Write a function named 'sum_prime_numbers' that takes an integer 'n' as input
# and returns the sum of all prime numbers less than or equal to 'n'.

# To solve this problem:
# 1. Determine if a number is prime.
# 2. Sum all the prime numbers that meet the condition.

# Specifications:
# - If 'n' is less than 2, the function should return 0 (no prime numbers less than 2).
# - The function should be as efficient as possible for large values of 'n'.

def is_prime(number):
    # If the number is less than 2, it's not prime
    if number < 2:
        return False

    # Check if the number is divisible by any number from 2 to its square root
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_prime_numbers(n):
    # If n is less than 2, return 0
    if n < 2:
        return 0

    # Initialize the sum at 0
    total = 0

    # Check every number from 2 up to n
    for number in range(2, n + 1):
        # If the number is prime, add it to the sum
        if is_prime(number):
            total += number

    return total

# Test the function with n = 7
n = int(input("Insert a number: "))
if is_prime(n):
    print(f"{n} is a prime number")
    booeleananswer = input ("Would you like to add all the numbers up to the specified number? yes/no ")
    if booeleananswer == "yes":
        result = sum_prime_numbers(n)
        print(f"The sum of the prime numbers up to {n} is: {result}")
    else:
        print("Thank you for using the program")
else:
    print(f"{n} is not a prime number")