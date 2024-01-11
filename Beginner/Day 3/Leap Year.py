year = int(input("Year to check if it is a leap year: "))

if year %4 == 0 and year %100 != 0 and year %400 != 0 :
    print("Leap Year")
else:
    print("Not a leap year")