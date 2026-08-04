playlist = ['晴天', '七里香', '晴天', '夜曲', '以父之名']
played = []
def playsongs(waiting , played):
    while waiting:
        song = waiting.pop()
        print(f'正在播放{song}')
        played.append(song)
playsongs(playlist , played )
print(playlist)
print(played)