# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)


# motorcycles.append('ducati')
# print(motorcycles)


# motorcyles = []

# motorcyles.append('honda')
# motorcyles.append('yamaha')
# motorcyles.append('suzuki')

# motorcyles.insert(0, 'ducati')

# print(motorcyles)

# del motorcyles[1]
# print(motorcyles)

# motorcyles.remove('suzuki')
# print(motorcyles)




guest_list = []


print(len(guest_list))

guest_list.append('Mandela')
guest_list.append('Tupac')
guest_list.append('Marley')

print(len(guest_list))

print(f'Welcome {guest_list} to the party')

new_guest = 'Kanye'
guest_list.remove('Marley')

guest_list.append(new_guest)
print(f'Welcome {guest_list} to the party')


guest_list.pop()
print(f'Welcome {guest_list} to the party')

del guest_list[:]
print(guest_list)
