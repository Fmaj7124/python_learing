prompt = '\nIf you could visit one place in the world,where would you go?'
places ={}
while True:
    #获取用户名字及想去的地方
    print(prompt)
    name = (input('Your name is: '))
    place = (input('The places you want to go: '))
    #将结果存住于字典places中
    places[name] = place
    #询问用户是否继续运行
    repeat = input('Would you like to let another person respond?(yes or no)')
    if repeat == 'no':
        break
print('The result is: ')
for name , place in places.items():
    print(f'{name} would like to go to {place}')