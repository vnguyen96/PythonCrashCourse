#8-6 City Names

def city_country(city, country):
    formatted_name = f"{city} , {country}"
    return formatted_name.title()

print(city_country('santiago', 'chile'))
print(city_country('saigon', 'vietnam'))
print(city_country('new york', 'USA'))

#8-7 Album

def make_album(artist_name, album, songs=None):
    album_info = {'artist': artist_name, 'album': album}
    if songs:
        album_info['songs'] = songs
    return album_info

artist_and_album = make_album('pink floy', 'the wall')
artist_and_album1 = make_album('pink floy', 'animals')
artist_and_album2 = make_album('pink floy', 'wywh', 4 )
print(artist_and_album)
print(artist_and_album1)
print(artist_and_album2)

#8-8 User Albums

def make_album(artist_name, album, songs=None):
    album_info = {'artist': artist_name, 'album': album}
    if songs:
        album_info['songs'] = songs
    return album_info

while True:
    #asking user to enter info
    user_input_artist = input('Enter artist name: ')
    user_input_album = input('Enter album name: ')
    user_input_songs = input("Enter number of songs on the album. If you don't know hit 'enter': ")

    if user_input_songs:
        artist_album_song = make_album(user_input_artist, user_input_album, user_input_songs)
        print(artist_album_song)
    else:
        artist_and_album = make_album(user_input_artist, user_input_album)
        print(artist_and_album)

    #if statement for exiting program
    exit_program = input("Enter 'quit' to exit program or 'continue' to add more: ")

    if exit_program == 'quit':
        break
    else:
        continue
