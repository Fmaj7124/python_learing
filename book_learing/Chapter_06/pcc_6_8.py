pet = {
    'Dog' : {
    'Name' : 'lucky' ,
    'fur_color' : 'white' ,
    'Master' : 'Kyrie' ,
    } ,

    'Cat' : {
    'Name' : 'Candy' ,
    'fur_color' : 'black' ,
    'Master' : 'Jean' ,
    } ,
}
for name , pet_info in pet.items():
    print(f'\nThe pet is a {name}')
    print(f"It's fur color is {pet_info['fur_color']}")
    print(F"The master of the pet is {pet_info['Master']}")

