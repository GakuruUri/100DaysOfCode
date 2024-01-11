#Tip Calculator
#Welcome to the calculator
print("Welcome to tip calculator \n")
#What is the total bill
bill = float(input("Enter Bill Amount: "))
#Enter % Tip
tip = float(input("Enter tip selected 1.1, 1.12 or 1.15%: "))
#How many People Split bill
split = int(input("Enter number of people sharing bill: "))
#Print Bill round 2

tip = bill * tip

total_bill ="{:.5f}".format( tip / split)

print(total_bill)

