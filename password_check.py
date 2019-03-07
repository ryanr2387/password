PASSWORD = 'Waubonsee'
user_password = input('Enter user password: ')

count = 1
while PASSWORD != user_password:
    print('INCORRECT PASSWORD')
    print(count)
    user_password = input('Enter user password: ')
    count = count + 1
    #print(count)

print('CORRECT')
