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


    #创建User的子类Admin
class Admin(User):
    def __init__(self , first_name , last_name , age , job):
        super().__init__(first_name , last_name , age , job)
        self.privileges=['can ban user.']

    """定义方法show_privileges"""
    def show_privileges(self):
        for privilege in self.privileges:
            print(F'As a admin,you can {privilege}')

    """定义方法add_privileges"""
    def add_privileges(self , new_privilege):
        self.privileges.append(new_privilege)

#创建一个admin实例并测试
admin1 = Admin('Tom' , 'Kevin' , '25' , 'teacher')
admin1.describe_user()