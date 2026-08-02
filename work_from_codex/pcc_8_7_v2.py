def pet_registry(name , type_of_pets , pet_age = None):
    registration_card = {'name' : name , 'Types of pets' : type_of_pets , }
    if pet_age is not None:
        pet_age = int(pet_age)
        registration_card['pet_age'] = pet_age
        return registration_card
    else:
        return registration_card

pet1 = pet_registry('煤球' , 'cat')
pet2 = pet_registry('豆豆' , 'dog' , 3)
pet3 = pet_registry('奶昔' , 'cat' , 0)
print (pet1)
print (pet2)
print (pet3)