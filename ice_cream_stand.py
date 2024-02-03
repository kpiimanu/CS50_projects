# Create a class for an ice cream stand that is a specific kind of restaurant
class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The {self.restaurant_name} is open!")

# The IceCreamStand is a child class to the restaurant parent class
class IceCreamStand(restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        """Add an attribute called flavors that stores a list of ice cream flavors"""
        self.flavors = ['Vanilla', 'Chocolate', 'Coffee', 'Mint']

    """write a method that displays these flavors"""
    def display_flavors(self):
        print(f"We serve the following flavors: {self.flavors}")

"""Create an instance of IceCreamStand and call this method"""
print("")
ice_cream = IceCreamStand('Fat Boys Ice Cream', 'Ice Cream Shop')
print(ice_cream.describe_restaurant())
ice_cream.display_flavors()
print("")
