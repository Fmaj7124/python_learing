list1 = ['jen' , 'jack' , 'Jame' , 'Kevin' , 'Jean']
favorite_languages ={
    'jen' : 'python' ,
    'jack':'c' ,
    'Jame' :'Java' ,
    'Kevin' : 'rust' ,
}
#用for循环list1从而到个人的名字(name)再将name放进favorite_languages中与Key判断
for name in list1:
    if name in favorite_languages:
        print (f'thx {name}')
    elif name not in favorite_languages:
        print ('请填写调查问卷')
