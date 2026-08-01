prompt ='Print quit to end programs'
while True:
    age = input(f'\nHow old are you? {prompt} ')
    if age =='quit':
        break
    age = int(age)
    if age <3:
        price=0
        print(f'You need to pay {price}')
    elif age <13:
        price = 10
        print(f'You need to pay {price}')
    else:
        price = 15
        print(f'You need to pay {price}')