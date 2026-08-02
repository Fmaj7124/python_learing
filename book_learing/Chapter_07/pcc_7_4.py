toppings =[]
prompt = '请输入您想添加的配料: '
while True:
    topping =input(prompt)
    if topping =='quit':
        break
    toppings.append(topping)
    print(toppings)