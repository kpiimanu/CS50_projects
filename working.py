import re
import sys


def main():
    print(convert(input("Hours: ")))
    sys.exit(0)


def convert(s):
    # Check if input is in correct format which includes making sure minutes inputted are optional and less than 60
    if not re.search(
        r"^(\d\d?)+(:[0-5][0-9])?(\s)+(AM|PM)(\s)to(\s)(\d\d?)+(:[0-5][0-9])?(\s)+(AM|PM)$",
        s,
    ):
        raise ValueError("Invalid input format")

    try:
        # Creating groups to access differnt parts of the time stamp
        if re.search(
            r"^(\d{1,2})(:(\d{2}))?\s*(AM|PM)\s*to\s*(\d{1,2})(:(\d{2}))?\s*(AM|PM)$", s
        ):
            time = re.search(
                r"^(\d{1,2})(:(\d{2}))?\s*(AM|PM)\s*to\s*(\d{1,2})(:(\d{2}))?\s*(AM|PM)$",
                s,
            )
            new_time = time.groups()
            # Running both start and end times through military_time function for conversion into 24hr time
            start_time_24 = military_time(new_time[0], new_time[2], new_time[3])
            end_time_24 = military_time(new_time[4], new_time[6], new_time[7])
            return start_time_24 + " to " + end_time_24

    except ValueError:
        sys.exit(1)


# Function to add 12 hours to the OG time unless the hour entered is 12
def military_time(hour, minute, am_pm):
    hour = int(hour)
    minute = int(minute) if minute else 0
    if minute == 60:
        raise ValueError("Invalid input: 60 minutes")
    elif am_pm == "PM" and hour != 12:
        hour += 12
    elif hour == 12 and am_pm == "AM":
        hour = 0
    return "{:02d}:{:02d}".format(hour, minute)


if __name__ == "__main__":
    main()