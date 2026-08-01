orders = ['杨枝甘露', '珍珠奶茶', '杨枝甘露', '柠檬茶', '杨枝甘露', '四季春']
print('抱歉，我们的杨枝甘露卖完了。')
#在orders中删除杨枝甘露
while '杨枝甘露' in orders:
    orders.remove('杨枝甘露')
    print(orders)
finished = []
#制作余下奶茶
while orders:
    finished_milktea = orders.pop()
    print(f'We already finish {finished_milktea}')
    finished.append(finished_milktea)
print(f'There are milk tea we finished: ')
#打印最终结果
print(f'{finished}')