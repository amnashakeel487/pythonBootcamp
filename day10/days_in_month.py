def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):

    month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    if is_leap(year) and month == 2:
        return 29

    return month_days[month - 1]


# Input
year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))

# Check for valid month
if month < 1 or month > 12:
    print("Invalid month!")
else:
    days = days_in_month(year, month)
    print(f"Number of days: {days}")