
def car_information(manufacturer , model , **car_info):
    car_info['Manufacturer']=manufacturer
    car_info['Model']=model
    return car_info

#打印一辆车的信息
car1 = car_information('BMW' , '535GT' ,
                colour = 'Black' ,
                interior_colour = 'black and brown' ,)
print(car1)