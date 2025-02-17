class Flight:
    def __init__(self, flight_number, departure, destination, price):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.price = price

    def display_info(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Departure: {self.departure}")
        print(f"Destination: {self.destination}")
        print(f"Price: ${self.price}")


class Booking:
    def __init__(self):
        self.passenger_name = ""
        self.flight = None

    def book_flight(self, name, flight):
        self.passenger_name = name
        self.flight = flight
        print(f"Booking Confirmed for {self.passenger_name}!")
        print(f"Flight details:")
        self.flight.display_info()


# Example Flights
flight1 = Flight("AI202", "New York", "Los Angeles", 200)
flight2 = Flight("AI203", "London", "Paris", 150)

# Simulating Booking
print("Welcome to Flight Booking System!")
name = input("Enter your name: ")
print("Available Flights:")
flight1.display_info()
flight2.display_info()

choice = input("Choose your flight by number (e.g., 'AI202'): ")

if choice == "AI202":
    booking = Booking()
    booking.book_flight(name, flight1)
elif choice == "AI203":
    booking = Booking()
    booking.book_flight(name, flight2)
else:
    print("Invalid flight number!")
