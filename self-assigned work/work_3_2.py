#游乐场门票机
active = True
while active:
    age = input("\nHow old are you?(Or enter 'quit' to end the program): ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 6:
            price='free'
            print(price)
        elif age < 18:
            price =20
            print(f'You need to pay {price}')
        elif age < 60:
            price = 50
            print(f'You need to pay {price}')
        else:
            price = 10
            print(f'You need to pay {price}')