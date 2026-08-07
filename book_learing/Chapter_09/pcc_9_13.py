from random import randint
class Die:
    def __init__(self , side=6):
        self.side = side

    #编写方法roll_die
    def roll_die(self):
        number = randint(1 , self.side)
        print(number)

    #编写一键投骰子的方法
    def roll_many(self, times):
        for _ in range(times):
            self.roll_die()

#创建实例并测试
dice1 = Die(6)
dice1.roll_die()
dice1.roll_many(20)

dice2 = Die(10)
dice2.roll_die()