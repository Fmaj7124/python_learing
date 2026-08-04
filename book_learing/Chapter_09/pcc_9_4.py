#创建类：Restaurant
class Restaurant:
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    #定义方法describe__restaurant方法
    def describe_restaurant(self):
        print(f'The name of this restaurant is{self.restaurant_name},'
              f'the cuisine in the restaurant is {self. cuisine_type}.')

    #定义方法open_restaurant()
    def open_restaurant(self):
        print(f'The {self.restaurant_name} is now open.')

    #定义方法change_numbers_served
    def change_numbers_served(self , change_number):
        self.numbers_served=change_number

    #定义方法read_numbers_served
    def read_numbers_served(self):
        print(f'There are {self.numbers_served} people that we served.')

    #定义方法increment_number_served
    def increment_number_served(self , new_number):
        self.numbers_served+=new_number
#创造实例并测试
restaurant1 = Restaurant('七欣天' , 'hot pot')
restaurant1.read_numbers_served()
restaurant1.change_numbers_served(100)
restaurant1.read_numbers_served()
restaurant1.increment_number_served(10)
restaurant1.read_numbers_served()