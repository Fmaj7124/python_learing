def build_profile(first , last , **user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

own_information =build_profile('Young' , 'Wang' ,
                               Height = '175cm' ,
                                Weight = '69kg')
print(own_information)