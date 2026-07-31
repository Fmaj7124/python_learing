cities = {
    'Hangzhou' : {
    'population' : '一千九百万' ,
    'Country' : 'China' ,
    'fact' : 'No delicious food' ,
    } ,

    'New York' :{
    'population' : '858万' ,
    'Country' : 'America' ,
    'fact' : 'Many mice' ,
    } ,

    'Paris' : {
    'population' : '204万' ,
    'Country' : 'France' ,
    'fact' :'Artist' ,
    } ,
}
for city_name , city_info in cities.items():
    print(f'\nThe city name is: {city_name}')
    print(f'The city population are:{city_info['population']}')
    print(f'The Country of the city:{city_info['Country']}')
    print(f'The fact of the city:{city_info['fact']}')