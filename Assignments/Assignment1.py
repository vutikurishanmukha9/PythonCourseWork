# Railway station
# Required data
# 1.Number of Persons travelling - integer
# 2.At what time the traveller will board the Train - Float
# 3.Destination place where we want to go - string
# 4.Source From where we want to go - string
# 5.Ticket Confirm or not - Boolean
# 6.Confimerd Seat Number - Tuple
# 7.Will the traveller Sacrifice the seat or not - Boolean
# 8.Seat the traveller might get - list
# 9.Will the traveller order the food or not - Boolean
# 10.If the traveller ordered the food what food will he ordered - Dictonary

# Collecting Inputs
Passenger_Count = int(input("Enter the Passenger count: "))
Passenger_Name = input("Enter the Passenger Name: ")
Boarding_time = float(input("Enter the Boarding Time of the passenger: "))
Destination_Station = input("Enter the Name of the Destination Station: ")
Boarding_station = input("Enter the Name of the Boarding Station: ")
Confirmed_Seat_Number = eval(input("Enter the Confirmed Seat Number as a tuple: "))
Willing_To_order_the_food = input("Will the passenger order food? (YES/NO): ").strip().upper()

# Ordered food input (only if YES)
Ordered_Food = {}
if Willing_To_order_the_food == "YES":
    print("Enter food in dictionary format. Example: {'Veg': 'Paneer Biryani', 'Drink': 'Lassi'}")
    Ordered_Food = eval(input("Enter the ordered food: "))

# Printing Outputs
print("\n--- Passenger Details ---")
print("Count of the Passenger travelling is:", Passenger_Count)
print("Name of the passenger travelling is:", Passenger_Name)
print("The Boarding Time of", Passenger_Name, "is:", Boarding_time)
print("The Destination station of the passenger is:", Destination_Station)
print("The Boarding station of the passenger is:", Boarding_station)
print("The Confirmed seat number of the Passenger is:", Confirmed_Seat_Number)
print("Will the passenger order food?", True if Willing_To_order_the_food == "YES" else False)
print("The ordered food of the passenger is:", Ordered_Food if Ordered_Food else "No food ordered.")


