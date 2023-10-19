#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
username = 'admin'
password = '12345'
user=''
pwd=''
while user!=username or pwd!=password:
    user=str(input('Enter username: '))
    user=user.strip()
    pwd=str(input('Enter password: '))
    pwd=pwd.strip()
    if user==username and pwd==password:
        print('Access granted!')
        break
    else:
        print('Access denied!')