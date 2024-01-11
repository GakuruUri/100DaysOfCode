def is_year_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            True
    else:
        False

# Example usage
print(is_year_leap(2000))
print(is_year_leap(1900))
print(is_year_leap(2016))
print(is_year_leap(2001))

def days_in_month(year, month):
    if not (isinstance (year, int) and 1 <= year <= 9999 ):
        return None
    if not ( isinstance (month, int) and 1 <= month <= 12 ):
        return None
        
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #Check if year is a leap year
    
    if month == 2 and ( year % 4 == 0 and ( year % 100 != 0 or year % 4 == 0 )):
        return 29
    
    return month_lengths [month - 1]

def day_of_year(year, month, day):

    if not (isinstance(year, int) and 1 <= year <= 9999):
        return None
    if not (isinstance(month, int) and 1 <= month <= 12):
        return None
    if not (isinstance(day, int) and 1 <= day <= 31):
        return None

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if year is a leap year
    if month == 2 and is_year_leap(year):
        month_lengths[1] = 29

    if day > month_lengths[month - 1]:
        return None

    return sum(month_lengths[:month-1]) + day

# Test cases
print(day_of_year(2000, 12, 31))  # Expected output: 366
print(day_of_year(2019, 1, 1))    # Expected output: 1
print(day_of_year(2020, 3, 1))    # Expected output: 61
print(day_of_year(2021, 2, 29))   # Expected output: None, 2021 is not a leap year


