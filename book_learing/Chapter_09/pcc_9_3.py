class User:
    def __init__(self , first_name , last_name , age , job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    #定义方法describe_user
    def describe_user(self):
        print(f"The user fullname is {self.first_name} {self.last_name},user's age is {self.age},job is {self.job}")

    #
    #定义方法greet_user
    def greet_user(self):
        print(f'Halo {self.first_name} {self.last_name}!')

#创建不同实例
user1 = User('Kanye' , 'West' , '49' , 'rapper/artist')
user2 = User('Taylor' , 'Swift' , '37' , 'singer')
user3 = User('Tom' , 'Holland' , '30' , 'actor')

#运行
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()