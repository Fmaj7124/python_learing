pizza_orders =['菠萝披萨' , '原味披萨' , '加州披萨' , '四季披萨']
finished_pizza =[]
while pizza_orders:
    current_pizza = pizza_orders.pop()
    print(f'I made your{current_pizza}')
    finished_pizza.append(current_pizza)
print(finished_pizza)
