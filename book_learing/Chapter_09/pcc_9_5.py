#获取用户信息
class User:
    def __init__(self , first_name , last_name , age , job):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.job=job
        self.login_attempts=0
    #定义方法describe_user
    def describe_user(self):
        print(f"The user fullname is {self.first_name} {self.last_name},user's age is {self.age},job is {self.job}")

    #定义方法greet_user
    def greet_user(self):
        print(f'Halo {self.first_name} {self.last_name}!')

    #定义方法increment_login_attempts
    def increment_login_attempts(self , login_attempts):
        self.login_attempts+=login_attempts

    #定义方法show_login_attempts
    def show_login_attempts(self):
        print(f'{self.login_attempts}')

    #定义方法reset_login_attempts
    def reset_login_attempts(self):
        self.login_attempts=0
#创建不同实例
user1 = User('Kanye' , 'West' , '49' , 'rapper/artist')
user2 = User('Taylor' , 'Swift' , '37' , 'singer')
user3 = User('Tom' , 'Holland' , '30' , 'actor' )

#test
user1.show_login_attempts()
user1.increment_login_attempts(1)
user1.show_login_attempts()
user1.reset_login_attempts()
user1.show_login_attempts()