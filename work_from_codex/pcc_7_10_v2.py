places = {}
print('你最想去的地方是哪里')
while True:
    #获取姓名与地点
    name = input('你的名字是: ')
    place = input('你最想去的地方是: ')
    #将信息添入字典（places）
    places[name] = place
    #询问是否继续
    repeat = input("你是否继续继续该程序(是/否)")
    if repeat == '否':
        break
#打印最终调查结果
print('调查结果为：')
print(f'{places}')
