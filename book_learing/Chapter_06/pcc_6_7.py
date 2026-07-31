people={
    'Speed' : {
    'first' : 'black' ,
    'last' : 'dick' ,
    'age' : '37' ,
    'city' : 'New York'
    } ,

    'spiderman' : {
        'first' : 'petter' ,
        'last' : 'parker' ,
        'age' : '30' ,
        'city' : 'New York' ,
    } ,

    'YE' : {
        'first' : 'kanye' ,
        'last' : 'west' ,
        'age' : '49' ,
        'city' : 'Chicago' ,
    },
}
for user_name , user_info in people.items():
    print (f'\nUsername:{user_name}')
    print(f'Fullname:{user_info['first'].title()}{user_info['last'].title()}')
    print(f'Age:{user_info['age']}')
    print(f'City:{user_info['city']}')