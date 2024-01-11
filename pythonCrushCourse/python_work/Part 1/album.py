""" 
8-7. Album: 
Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
"""

def make_album(artist_name, album_name):
    """Return formatted album name"""
    album = {'Name': artist_name, 'Album': album_name}
    return album

make_album_artist = make_album(album_name='Survivor', artist_name='Bob Marley')
print(make_album_artist)
make_album_artist = make_album('Stanley and the Turbines', 'Kalalou')
print(make_album_artist)



# Second solution

def make_album(artist, title, songs=None):
    """Return album dictionary."""
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album

print(make_album("Michael Jackson", 'Thriller'))
print(make_album("The Beatles", "Let it be", 12))


""" 
8-8. User Albums: 
Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
"""


# use a while loop in the above.

def make_album(artist, title, songs=None):
    """Return album dictionary."""
    album = {'artist': artist, 'title': title, 'songs':songs}
    return album

while True:
    print("\nEnter album information.")
    print("(enter 'q' at any time to quit)")
    
    artist = input("Enter Artist name: ")
    if artist == 'q':
        break
    
    title = input("Enter Title of album: ")
    if title == 'q':
        break
    
    song = input("Enter Songs number(optional): ")
    if song == 'q':
        break
    
    album = make_album(artist, title, song)
    print(album)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    