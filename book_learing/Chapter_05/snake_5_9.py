User_names = ['Tom' , 'Kevin' , 'Paul' , 'admin' , 'Micheal']
if User_names:
    for User_name in User_names:
        if User_name =='admin':
            print ('Hello admin,would you like to see status report?')
        else:
            print (f'Hello {User_name},thank you for logging again.')
        #误打误撞触发if else 语句了。
else:
    print('We need to find more user!')

