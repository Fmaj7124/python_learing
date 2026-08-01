prompt ='Print quit to end programs'
active = True
while active:
    age = input(f'\nHow old are you? {prompt} ')
    if age =='quit':
        active = False
    else:
        age = int(age)
        if age <3:
            price=0
            print('Free')
        elif age <13:
            price = 10
            print(f'You need to pay {price}')
        else:
            price = 15
            print(f'You need to pay {price}')