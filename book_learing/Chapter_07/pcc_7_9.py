pizza_orders =['pastrami' ,  '菠萝披萨' , '原味披萨' ,'pastrami' , '加州披萨' , '四季披萨',
                        'pastrami']
print('pastrami已经卖完了')
while 'pastrami' in pizza_orders:
    pizza_orders.remove('pastrami')

print(pizza_orders)