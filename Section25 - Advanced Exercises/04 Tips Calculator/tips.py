#Tips Calculator
#Ticket Price
#Tip Percentage
#People to Share

from uu import Error

print ("Welcome to the Tip Calculator")
ticket = float(input("Please enter the total amount of the bill: "))
print("Thank you!")
tip = int(input("Please enter the percentage you would like to tip: "))
print("Awesome")
people = int(input("Please enter the number of people to split the bill with: "))
print("Thank you!")

def calculate_tip(ticket,tip,people):
    try:
        percentage = (tip*ticket)/100
        print(f"\n The tip amount is {percentage:.2f} USD")

        total_amount_with_tip = ticket+percentage
        print(f"\n The total amount including the tip is {total_amount_with_tip:.2f} USD")

        split_ticket = total_amount_with_tip/people
        print(f"\n Each person should pay {split_ticket:.2f} USD")
    
    except Exception as e:
        print(f"An error ocurred {e}")

calculate_tip(ticket,tip,people)
