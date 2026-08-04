#创建类：Restaurant
class Restaurant:
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #定义方法describe__restaurant方法
    def describe_restaurant(self):
        print(f'The name of this restaurant is{self.restaurant_name},'
              f'the cuisine in the restaurant is {self. cuisine_type}.')

    #定义方法open_restaurant()
    def open_restaurant(self):
        print(f'The {self.restaurant_name} is now open.')

#创建一个实例以测试
restaurant1 = Restaurant('七欣天' , 'hot pot')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
