def make_album(album_title , singer_name , songs_numbers = None):
    album = {'name' : album_title , 'artist' : singer_name ,}
    if songs_numbers:
        album['songs'] = songs_numbers
        return album
    else:
        return album

album1 = make_album('YE' , 'Kanye')
print(album1)
album2 = make_album('叶惠美' , 'Jaychou' , 11)
print(album2)
album3 = make_album('1989' , 'Taylor')
print(album3)