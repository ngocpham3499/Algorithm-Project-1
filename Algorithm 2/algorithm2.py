# Name: Ngoc Pham
# Email: ngocpham3499@csu.fullerton.edu

def preferredCity(city_distances, fuel, mpg):

    total_fuel = 0          # Total amount of fuel across all cities
    current_fuel = 0        # Current amount of fuel while traversing each city
    preferred_start = 0     # Index of the starting city

    # Iterate through each city and calculate the net fuel after visiting city i
    for i in range(len(city_distances)):
        net_fuel = (fuel[i] * mpg) - city_distances[i]
        
        # Update the total and current fuel tank
        total_fuel += net_fuel
        current_fuel += net_fuel
        
        # If the current fuel is less than zero, update the current_fuel and reset the fuel tank amount
        if current_fuel < 0:
            preferred_start = i + 1
            current_fuel = 0

    # Check if total fuel is non-negative and return the index of the best starting city
    if total_fuel >= 0:
        return preferred_start % len(city_distances)
    else:
        # Starting city does not exist
        return -1

# Testing the function using sample input example
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Find and print the preferred starting city
print("City Distances:", city_distances)
print("Fuel at each city:", fuel)
print("Miles per gallon (mpg):", mpg)
preferred_city = preferredCity(city_distances, fuel, mpg)
print(f"The preferred starting city is city {preferred_city}")
