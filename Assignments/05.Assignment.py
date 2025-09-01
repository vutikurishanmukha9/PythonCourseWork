# Very Simple Railway Station OOP System

# ============= 1. PARENT CLASS =============
class Train:
    """Parent class for trains"""
    
    # CLASS ATTRIBUTES - shared by all trains
    railway_name = "Indian Railways"
    total_trains = 0
    
    def __init__(self, train_number, train_name):
        # INSTANCE ATTRIBUTES - unique for each train
        self.train_number = train_number
        self.train_name = train_name
        Train.total_trains += 1
    
    # INSTANCE METHOD
    def start_journey(self):
        return f"Train {self.train_name} is starting"
    
    # CLASS METHOD
    @classmethod
    def get_total_trains(cls):
        return cls.total_trains
    
    # STATIC METHOD
    @staticmethod
    def format_time(time_float):
        hours = int(time_float)
        minutes = int((time_float - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"

# ============= 2. CHILD CLASSES (INHERITANCE) =============
class ExpressTrain(Train):
    """Child class - inherits from Train"""
    
    def __init__(self, train_number, train_name):
        super().__init__(train_number, train_name)  # SUPER() - call parent
        self.speed = "Fast"
    
    # POLYMORPHISM - same method name, different behavior
    def start_journey(self):
        return f"Express Train {self.train_name} starting fast!"

class LocalTrain(Train):
    """Child class - inherits from Train"""
    
    def __init__(self, train_number, train_name):
        super().__init__(train_number, train_name)  # SUPER() - call parent
        self.speed = "Slow"
    
    # POLYMORPHISM - same method name, different behavior  
    def start_journey(self):
        return f"Local Train {self.train_name} starting slowly!"

# ============= 3. PASSENGER CLASS (Your Original Requirements) =============
class Passenger:
    """Based on your original railway station code"""
    
    # CLASS ATTRIBUTES
    total_passengers = 0
    
    def __init__(self, name, age):
        # INSTANCE ATTRIBUTES - from your original code
        self.name = name
        self.age = age
        self.passenger_count = 1
        self.boarding_time = None
        self.destination_station = ""
        self.boarding_station = ""
        self.confirmed_seat_number = None
        self.ticket_confirmed = False
        self.will_sacrifice_seat = False
        self.possible_seats = []
        self.willing_to_order_food = False
        self.ordered_food = {}
        
        Passenger.total_passengers += 1
    
    # INSTANCE METHODS
    def set_journey(self, boarding_time, source, destination):
        self.boarding_time = boarding_time
        self.boarding_station = source
        self.destination_station = destination
    
    def confirm_seat(self, seat_tuple):
        self.confirmed_seat_number = seat_tuple
        self.ticket_confirmed = True
    
    def order_food(self, food_dict):
        self.ordered_food = food_dict
        self.willing_to_order_food = True
    
    def show_details(self):
        print("--- Passenger Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Count: {self.passenger_count}")
        print(f"Boarding Time: {Train.format_time(self.boarding_time) if self.boarding_time else 'Not Set'}")
        print(f"Source: {self.boarding_station}")
        print(f"Destination: {self.destination_station}")
        print(f"Confirmed Seat: {self.confirmed_seat_number}")
        print(f"Ticket Status: {'Confirmed' if self.ticket_confirmed else 'Pending'}")
        print(f"Will Order Food: {self.willing_to_order_food}")
        print(f"Ordered Food: {self.ordered_food if self.ordered_food else 'No food ordered'}")
    
    # CLASS METHOD
    @classmethod
    def get_total_passengers(cls):
        return cls.total_passengers

# ============= 4. CHILD PASSENGER CLASSES (INHERITANCE) =============
class SeniorCitizen(Passenger):
    """Child class for senior citizens"""
    
    def __init__(self, name, age):
        super().__init__(name, age)  # SUPER()
        self.discount = 50
    
    # POLYMORPHISM - extending parent method
    def show_details(self):
        super().show_details()  # SUPER() - call parent method
        print(f"Senior Citizen Discount: {self.discount}%")

# ============= 5. SIMPLE USER INPUT (Like Your Original) =============
def take_user_input():
    """Take input from user - exactly like your original code"""
    
    print("🚂 Railway Booking System")
    print("=" * 30)
    
    # Basic passenger details
    name = input("Enter Passenger Name: ")
    age = int(input("Enter Passenger Age: "))
    
    # Create passenger (INHERITANCE based on age)
    if age >= 60:
        passenger = SeniorCitizen(name, age)
        print(f"Senior citizen created with {passenger.discount}% discount!")
    else:
        passenger = Passenger(name, age)
    
    # Journey details (your original inputs)
    boarding_time = float(input("Enter Boarding Time (e.g. 15.20): "))
    source = input("Enter Boarding Station: ")
    destination = input("Enter Destination Station: ")
    
    # Set journey using INSTANCE METHOD
    passenger.set_journey(boarding_time, source, destination)
    
    # Seat details (your original format)
    seat_input = input("Enter Confirmed Seat (e.g. S1,45): ")
    try:
        coach, seat_num = seat_input.split(",")
        passenger.confirm_seat((coach.strip(), int(seat_num.strip())))
    except:
        print("Invalid seat format!")
    
    # Food order (your original format)
    food_choice = input("Will you order food? (YES/NO): ").upper()
    if food_choice == "YES":
        print("Enter food like: Chicken Biryani")
        main_food = input("Enter main food: ")
        drink = input("Enter drink: ")
        food_dict = {"Main": main_food, "Drink": drink}
        passenger.order_food(food_dict)
    
    return passenger

def select_train():
    """Simple train selection"""
    print("\nSelect Train Type:")
    print("1. Express Train")
    print("2. Local Train")
    
    choice = input("Enter choice (1/2): ")
    train_number = int(input("Enter train number: "))
    train_name = input("Enter train name: ")
    
    if choice == "1":
        return ExpressTrain(train_number, train_name)  # INHERITANCE
    else:
        return LocalTrain(train_number, train_name)    # INHERITANCE

# ============= 6. MAIN PROGRAM =============
def main():
    """Main program - simple and clear"""
    
    # Show OOP concepts working
    print("="*40)
    print("RAILWAY STATION OOP CONCEPTS")
    print("="*40)
    
    # STATIC METHOD demo
    print(f"Static Method - Format time 15.45: {Train.format_time(15.45)}")
    
    # CLASS ATTRIBUTE demo
    print(f"Class Attribute - Railway: {Train.railway_name}")
    
    # Create train - INHERITANCE and POLYMORPHISM
    print(f"\nInitial trains: {Train.get_total_trains()}")  # CLASS METHOD
    
    # Get user input
    print("\n" + "="*40)
    selected_train = select_train()
    passenger = take_user_input()
    
    # Show POLYMORPHISM - same method, different behavior
    print(f"\n🚂 {selected_train.start_journey()}")
    
    # Final display using POLYMORPHISM
    print(f"\n📊 Final Booking Details:")
    print(f"Train: {selected_train.train_name} ({selected_train.speed} speed)")
    passenger.show_details()  # Will show discount for senior citizens
    
    # CLASS METHOD demo
    print(f"\n📈 Statistics:")
    print(f"Total trains: {Train.get_total_trains()}")
    print(f"Total passengers: {Passenger.get_total_passengers()}")
    
    print(f"\n✅ Booking completed successfully!")

# Run the program
if __name__ == "__main__":
    main()