# A program that prompts for a time and outputs the meal time

# Function to convert time from str to float
def convert(time):
    hours, minutes = time.split(":")
    # Convert hours into float
    hours = float(hours)
    # Convert minutes into float
    minutes = float(minutes)/60
    # Merge both floats to create time float
    time = hours + minutes
    return time

# Main code prompting user for time
def main():
    time_str = input("What time is it? ")
    # Run time function to convert input into float
    time = convert(time_str)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")
    else:
        return 1

if __name__ == "__main__":
    main()