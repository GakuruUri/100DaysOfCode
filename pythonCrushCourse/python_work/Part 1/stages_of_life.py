age = 20

if age < 2:
    print("That person is a baby")
elif age > 2 and age <= 4:
    print("That person is toddler")
elif age > 4 and age <= 13:
    print("That person is a kid")
elif age > 13 and age <= 20:
    print("That person is a teenager")
elif age > 20 and age <= 65:
    print("That person is an adult")
    
else:
    print("That person is an elder")



age = 21

if age <= 2:
    life = 'a baby'
elif age > 2 and age <= 4:
    life = 'a toddler'
elif age > 4 and age <= 13:
    life = 'a kid'
elif age > 13 and age <= 20:
    life = 'a teenager'
elif age > 20 and age <= 65:
    life = 'an adult'
else:
    life = 'an elder'
    
print(f"This person is {life}.")

