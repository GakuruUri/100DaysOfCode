# You'll need to figure out how you want to structure your dictionary.
# You'll need a way to enter more than one names; otherwise, there's only going to be ONE name in your dictionary.
# I've structured my code to have the name as key and the age as value. I allow user to enter more than one name simply by asking if they want to add more and use a while loop to check against that. You'll need to implement a check to see whether the user has enter an age.

def collect_names ():
     info = {}
     total_age = 0
     answer = 'y'
     while answer == 'y':
         name = input('Enter a name: ')
         info [name] = int (input('Enter an age: '))
         answer = input ('Enter more names? ').lower ()
     for name in info:
         total_age += info [name]
     person_count = len (info)
     avg_age = total_age / float (person_count)
     return person_count, avg_age

count, avg = collect_names()
# Enter a name: John Doe
# Enter an age: 21
# Enter more names? y
# Enter a name: Jane Doe
# Enter an age: 29
# Enter more names? y
# Enter a name:James Smith
# Enter an age: 25
# Enter more names? n
