orders = ['珍珠奶茶', '柠檬茶', '乌龙奶茶', '四季春']
finished = []
#制作
while orders:
    finished_milktea = orders.pop()
    print(f'We already finish {finished_milktea}')
    finished.append(finished_milktea)
print(f'There are the milk tea we finished: ')
print(f'{finished}')
