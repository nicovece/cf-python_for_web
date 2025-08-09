class Date():
    def __init__(self, name, day, month, year):
        self.name = name
        self.day = day
        self.month = month
        self.year = year
    
    def get_date(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    def set_date(self):
        self.day = int(input("Enter the day of the month: "))
        self.month = int(input("Enter the month: "))
        self.year = int(input("Enter the year: "))

    # A custom method that tells us if we're on a leap year (this is
    # normally a more complex method; we've simplified it here)
    def is_leap_year(self):
        return self.year % 4 == 0

    # This function checks if our date is valid or not.
    def is_valid_date(self):
        # Here, we'll check if a few conditions are met
        # to verify if our date is valid. If any of them aren't
        # satisfied, the function directly returns "False".

        # First, we check if the values are all integers
        if not (type(self.day) == int and type(self.month) == int and type(self.year) == int):
            return False

        # Next, we make sure that the year isn't negative.
        if self.year < 0:
            return False

        # After this we check if the given month is between 1 and 12.
        if self.month < 1 or self.month > 12:
            return False

        # Our next step is to verify if the day is valid for a given month.
        # We'll list out the last dates for each month in a dictionary -
        # The keys are months, and the values are the number of days
        # in their corresponding months.
        last_dates = {
            1: 31,
            2: 29 if self.is_leap_year() else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        # Finally, we verify if the day is valid for the given month.
        if self.day < 1 or self.day > last_dates.get(self.month):
            return False

        # If none of the above if statements triggered
        # the 'return False' statements, the script reaches this
        # point where it returns True.
        return True
    


# first_moon_landing = Date("Apollo 11", 20, 7, 1969)

# print(first_moon_landing.get_date())
# print(first_moon_landing.name)

# first_moon_landing.set_date()

# print(first_moon_landing.get_date())

date1 = Date("date_1", 29, 2, 2000)  
date2 = Date("date_2", 29, 2, 2001)
date3 = Date("date_3", "abc", "def", "ghi")   

print(str(date1.get_date()) + ": " + str(date1.is_valid_date()))
print(str(date2.get_date()) + ": " + str(date2.is_valid_date()))
print(str(date3.get_date()) + ": " + str(date3.is_valid_date()))