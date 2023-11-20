#leap year 2
# On every year that is divisible by 4
   #Except every year that is evenly divisible by 100
      #Unless the year is also evenly divisible by 100

year = int(input ("Enter year to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")