movie_ratings = {
    'Dave' :'教父'  ,
    'Kevin' : '绿皮书' ,
    'Michael' :'蜘蛛侠' ,
}
friend_to_check = ['Dave' , 'Kevin' ,'Michael' , 'Jackson' , 'Tyler']
#检查是否再movie_ratings的对应的键中
for name in friend_to_check:
    if name in movie_ratings.keys():
        movie = movie_ratings[name]
        print(f'{name}推荐了{movie}，我也很喜欢这部电影')
    elif name not in movie_ratings:
        print(f'{name}还没有推荐电影')