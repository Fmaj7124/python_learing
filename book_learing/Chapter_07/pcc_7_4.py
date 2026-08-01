toppings =[]
prompt = '请输入您想添加的配料: '
while True:
    topping =input(prompt)
    toppings.append(topping)
    print(toppings)
    if topping =='quit':
        break