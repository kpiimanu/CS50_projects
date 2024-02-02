# Write a function that stores information about a car in a dicitonary
# Must always include maufacture name and model name
# arbitrary keyword arguments

def car_info(manufacture_name, model_name, **car_details):
    car_details['Manufacture Name'] = manufacture_name
    car_details['Model Name'] = model_name
    return car_details

car_details = car_info('Subaru', 'Outback', color='blue', tow_package=True)

print(f"\n{car_details}") 
print("")   