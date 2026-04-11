from datetime import datetime, timedelta

def get_next_birthday(birthday):
    today = datetime.today()
    # Replace year with current year
    next_birthday = birthday.replace(year=today.year)
    
    # If birthday already occurred this year, set it to next year
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    
    return next_birthday

# Input birthday in YYYY-MM-DD format
dob_input = input("Enter your birthday (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d")

# Calculate age
today = datetime.today()
age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age = 1

# Get time until next birthday
next_birthday = get_next_birthday(dob)
time_left = next_birthday - today

# Convert time difference into components
days = time_left.days
seconds_left = time_left.seconds
hours = seconds_left // 3600
minutes = (seconds_left % 3600) // 60
seconds = seconds_left % 60

# Output
print(f"\nYou are {age} years old.")
print(f"Time until your next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")