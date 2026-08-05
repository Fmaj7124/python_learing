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
        self.privileges = Privileges()
    """创建类privileges"""
class Privileges:
    def __init__(self):
        self.privileges = ['can ban user.']

    def describe_privileges(self):
        for privileges in self.privileges:
            print(f'Your privileges is {privileges}')

        """定义方法add_privileges"""
    def add_privileges(self , new_privileges):
        self.privileges.append(new_privileges)

#创建一个admin实例并测试
admin1 = Admin('Tom' , 'Kevin' , '25' , 'teacher')
admin1.describe_user()
admin1.privileges.add_privileges('can add post')
admin1.privileges.describe_privileges()