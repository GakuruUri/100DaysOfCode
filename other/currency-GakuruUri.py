yuan = int(input ("What do you have left in yuan: "))
yen= int(input ("What do you have left in yen: "))
won = int(input ("What do you have left in won: "))

#convert currencies

# dyuan = float(yuan * 0.14)
# dyen = float(yen * 0.0073)
# dwon = float(won * 0.00077)

total = yuan * 0.15 + yen * 0.0077 + won * 0.00080

# last_dollars = (dyuan + dyen + dwon)

print(f"Remaining cash is = {total} ")
