
#不断向用户提问以获取数据, 直到用户退出
while True:
    number1 = (input("请输入第1个加数(输入'q'以退出)"))
    if number1 == 'q':
        break
    number2 = (input("请输入第2个加数(输入'q'以退出)"))
    if number2 =='q':
        break

    try:
        number1 = int(number1)
        number2 = int(number2)
        result = number1 + number2
    except ValueError:
        print('请输入数字！')
    else:
        print(f'结果为{result}')