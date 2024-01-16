# Define the hotel_cost() function
def hotel_cost(num_nights):
    price_per_night = 100 # Set the price per night to $100
    return num_nights * price_per_night

# Define the plane_cost() function
def plane_cost(city_flight):
    if city_flight == "New York":
        return 500 # Flight to New York costs $500
    elif city_flight == "Chicago":
        return 400 # Flight to Chicago costs $400
    elif city_flight == "Los Angeles":
        return 600 # Flight to Los Angeles costs $600
    else:
        return 0 # For all other cities, return $0 (invalid)

# Define the car_rental() function
def car_rental(rental_days):
    daily_rental_cost = 50 # Set the daily rental cost to $50
    return rental_days * daily_rental_cost

# Define the holiday_cost() function
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Main program
print("Welcome to the holiday cost calculator!")
city_flight = input("Enter city of flight (New York, Chicago, Los Angeles): ")
num_nights = int(input("Enter number of nights in hotel: "))
rental_days = int(input("Enter number of car rental days: "))

total_hotel_cost = hotel_cost(num_nights)
total_plane_cost = plane_cost(city_flight)
total_car_rental_cost = car_rental(rental_days)
total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_car_rental_cost)

if total_holiday_cost > 0:
    print(f"Your total hotel cost for {num_nights} nights is ${total_hotel_cost}.")
    print(f"Your total flight cost for {city_flight} is ${total_plane_cost}.")
    print(f"Your total car rental cost for {rental_days} days is ${total_car_rental_cost}.")
    print(f"Your total holiday cost is ${total_holiday_cost}.")
else:
    print("Invalid city of flight. Please try again.")