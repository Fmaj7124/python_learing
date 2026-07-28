pizzas = ['pizza1' , 'pizza2' , 'pizza3']
for pizza in pizzas:
    print(f'I like {pizza}')
print('I love pizza!!!')
pizzas = pizzas[:]
friends_pizzas =pizzas[:]
pizzas.append('pizza4')
friends_pizzas.append('pizza5')
print(f'My pizzas are:{pizzas}')
print(f'My friends pizzas are:{friends_pizzas}')
for friend in friends_pizzas:
    print(friend)
