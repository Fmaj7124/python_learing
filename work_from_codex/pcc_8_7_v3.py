def player_information (name , job , level = None):
    player_card ={'name' : name , 'job' : job , }
    if level is not None:
        level = int(level)
        player_card['level'] = level
        return player_card
    else:
        return player_card
    #登记用户信息
player1 = player_information('阿岚' , '法师')
player2 = player_information('小湖' , '战士' , 25)
player3 = player_information('小夜' , '刺客' , 0)
print(player1)
print(player2)
print(player3)
#DeepSeek都取的什么2B名字。