# Calculating are of a circle

print('Specify x To Close Program! ')

while True:
    rad = input('Enter Radius of Circle: ')
    if rad == 'x':
        break
    else:
        radius = float(rad)
        area = 3.14 * radius * radius
        print('The Area of The Circle is: ' + str(area))