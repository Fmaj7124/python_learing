def make_album(album_title , singer_name , song):
    album = {'name' : album_title , 'artist' : singer_name , 'songs_numbers'  : song}
    return album

#编写while循环从用户中获取信息
while True:
    album_name = input("请输入专辑名(输入'q'以退出)")
    if album_name == 'q':
        break
    singer = input("请输入歌手名(输入'q'以退出)")
    if singer == 'q':
        break
    songs = input("请输入该专辑的歌曲数(输入'q'以退出)")
    if songs == 'q':
        break
    songs = int(songs)
    message = make_album(album_name, singer , songs)
    print(message)