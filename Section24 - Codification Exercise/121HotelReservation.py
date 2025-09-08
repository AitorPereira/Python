# Hotel Reservations
# Description:
#
# You are going to develop a function that simulates a hotel room reservation management system.
# The system should be able to perform the following operations:
#
# Reserve a room: Reserve a room for a customer on a specific date.
# Cancel a reservation: Cancel an existing reservation.
# Check availability: Check if a room is available on a specific date.
# List reservations: List all existing reservations.
#
# Function Requirements:
#
# The main function will be called manage_reservations and will take two parameters:
#
# operation: a string indicating the operation to perform ("reserve", "cancel", "check", "list").
# details: a dictionary containing the necessary details for the operation.
#
# Reservations will be stored in a list of dictionaries, where each dictionary represents a reservation
# with the following details: customer, room, date.

reservations = []

def manage_reservations(operation,details,reservations=None):
    if reservations==None:
        reservations=[]

    if operation == "reserve":
        reservation = {
            'customer' : details['customer'],
            'room' : details['room'],
            'date' : details['date']
        }
        reservations.append(reservation)
        print("Reservation succesful")
        print(f"Details of reservation: {reservation}")
        return reservations

    elif operation == "cancel":
        for res in reservations:
            if (res["customer"] == details["customer"] and res["room"] == details["room"] and res ["date"] == details["date"]):
                reservations.remove(res)
                print ("Reservation Canceled")
                return reservations
        print ("Reservation not found")

    elif operation == "check":
        for res in reservations:
            if (res["room"] == details["room"] and res["date"] == details["date"]):
                mensaje = f"Room {details['room']} is already booked on {details['date']}"
                return mensaje

        mensaje = f"Room {details['room']} is available on {details['date']}"
        return mensaje
    
    elif operation == "list":
        if reservations:
            print ("Current Reservations: ")
            for res in reservations:
                print (res)
        else:
            print("No reservations has been made")
    
    else:
        print("Invalid operation")
    
    return reservations



# --------------------
# 🔄 Test Cases Below
# --------------------

# # Make a reservation
# reservations = manage_reservations(
#     "reserve", {
#     "customer": "Aitor Martínez",
#     "room": "101",
#     "date": "2025-09-10"
# }, reservations)

# # Check availability
# manage_reservations(
#     "check", {
#     "room": "101",
#     "date": "2025-09-10"
# }, reservations)

# # Cancel reservation
# reservations = manage_reservations(
#     "cancel", {
#     "customer": "Aitor Martínez",
#     "room": "101",
#     "date": "2025-09-10"
# }, reservations)

# # List all
# manage_reservations("list", {}, reservations)


reservations = []

# 1. Make a reservation
reservations = manage_reservations("reserve", {"customer": "Pedro Ramirez", "room": "109", "date": "2025-09-10"}, reservations)
# Expected output:
# Reservation succesful
# Details of reservation: {'customer': 'Pedro Ramirez', 'room': '109', 'date': '2025-09-10'}

# 2. Check room availability for the same room and date
availability = manage_reservations("check", {"room": "109", "date": "2025-09-10"}, reservations)
print(availability)
# Expected output:
# Room 101 is already booked on 2025-09-10

# # 3. Try to make a reservation for a different room and date
reservations = manage_reservations("reserve", {"customer": "Maria Gomez", "room": "102","date": "2025-09-11"}, reservations)
# # Expected output:
# # Reservation succesful
# # Details of reservation: {'customer': 'Maria Gomez', 'room': '102', 'date': '2025-09-11'}

# # 4. Cancel an existing reservation
reservations = manage_reservations("cancel", {"customer": "Aitor Martínez","room": "101","date": "2025-09-10"}, reservations)
# # Expected output:
# # Reservation Canceled

# # 5. Try to cancel a non-existent reservation
reservations = manage_reservations("cancel", {"customer": "Non Existent","room": "999","date": "2025-01-01"}, reservations)
# # Expected output:
# # Reservation not found

# 6. Check availability for a room and date with no reservations
availability = manage_reservations("check", {"room": "101", "date": "2025-09-10"}, reservations)
print(availability)
# Expected output:
# Room 101 is available on 2025-09-10

# 7. List all current reservations
manage_reservations("list", {}, reservations)
# Expected output:
# Current Reservations: 
# {'customer': 'Maria Gomez', 'room': '102', 'date': '2025-09-11'}

# 8. Use invalid operation
manage_reservations("invalid_op", {}, reservations)
# Expected output:
# Invalid operation

