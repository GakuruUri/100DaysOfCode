veggies = ['cucumber', 'managu', 'terere', 'cabbage']
print('Is veggeies == "malenge"? I predict False.')
print(veggies == 'malenge')
for vegetables in veggies:
    if vegetables == 'malenge':
       True
        
    else:
        False
        
print('Is veggeies == "cucumber"? I predict True.')
print(veggies == 'cucumber')  
if 'cucumber' in veggies:
    print(True)
else:
    print(False)

print('Is veggeies == "Daagaa"? I predict False.')
print(veggies == 'daagaa')
if 'daagaa' in veggies:
    print(True)
else:
    print(False)
    
    

daughters = ['wanjiru', 'wangari', 'wambui', 'watiri']
print('Is daughters == "Wainaina"? I predict False.') 
print(daughters == 'wainaina')
for daughter in daughters:
    if daughter == 'Wainaina':
        True
        
    else:
        False
    
if daughter == 'Wainaina' and daughter == 'watiri':
    print(True)
else:
    print(False)
    


print('\nIs daughters == "wambui"? I predict False.') 
print(daughter == 'wambui')

if daughter == 'wambui' or daughter == 'njuguna':
    print(True)
    
else:
    print(False)
    
    
    
    
if 'wambui' in daughters:
    print(True)
else:
    print(False)
    
    
    
if 'kiprotich' in daughter:
    print(True)
else:
    print(False)