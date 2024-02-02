# Create a class called restaurant w/ 2 init attributes: restaurant_name & restaurant_cuisine

class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The {self.restaurant_name} is open!")

# Create 3 different instances from this class & describe_restaurant for each instance
print('')
west_side = restaurant('Mama Bear', 'Sandwiches')
west_side.describe_restaurant()
print('')
south_side = restaurant('Kauai Poke Co.', 'Seafood')
south_side.describe_restaurant()
print('')
east_side = restaurant('Leongs Meat House', 'Local')
east_side.describe_restaurant()
print('')