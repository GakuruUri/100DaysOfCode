#Age Cslculator in days, months, years
age=int(input("Enter your current age: "))

age_rem = 90-age

age_days = (age_rem*365)
age_weeks = (age_rem*52)
age_months = (age_rem*12)

answer = f"You have {age_days} days, {age_weeks} weeks, {age_months} months left! "

print(answer)