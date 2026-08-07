from random import choice
ticket = ['10' , 'A' , '12' , '4' , 'B' , '7' , '23' , 'C' , '72' , 'D' , 'E' , '21' , '45' , '92' , '32']
winning_ticket=[]
#选取中奖彩票
for _ in range(4):
    draw = choice(ticket)
    winning_ticket.append(draw)

print(f'如果你抽中了{winning_ticket}，就牛逼中大奖了')

attempts = 0
#刮彩票直到中奖
while True:
    attempts+=1
    my_ticket = []
    for _ in range(4):
        draw = choice(ticket)
        my_ticket.append(draw)
    print(my_ticket)
    if my_ticket == winning_ticket:
        break
print(f'I used {attempts}')