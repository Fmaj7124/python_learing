current_users = ['Tom' , 'Kevin' , 'Paul' , 'admin' , 'Michael']
current_users_lower=[user.lower() for user in current_users]
new_users=['Tom' , 'Sam' , 'Kevin' , 'Bill' , 'Sherry']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print ('Please make another name.')
    else:
        print('This is a new name.')
