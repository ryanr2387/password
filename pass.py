PASSWORD = 'Waubonsee'
user_password = input('Enter user password: ')

while PASSWORD != user_password:
    print('INCORRECT PASSWORD')
    user_password = input('Enter user password: ')

print('CORRECT')