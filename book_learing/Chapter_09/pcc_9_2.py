class Restaurant:
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #定义方法describe__restaurant方法
    def describe_restaurant(self):
        print(f'\nThe name of this restaurant is {self.restaurant_name},'
              f'the cuisine in the restaurant is {self. cuisine_type}.')

    #定义方法open_restaurant()
    def open_restaurant(self):
        print(f'The {self.restaurant_name} is now open.')


# 创建一个实例以测试
restaurant1 = Restaurant('七欣天', 'hot pot')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('沙县小吃' , '炒牛肉')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('兰州拉面' , '牛肉面')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()