#QUESTION1

user_name = "serkan"
password ="123456"

user_name1 =input("Please enter your user name: ")

password1= input("Please enter your password: ")

if (user_name != user_name1 and password == password1):
    print("Invalid user name")
elif (user_name==user_name1 and password != password1):
    print("Invalid Password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("You are now logged in...")
    
    
    
    #USING DICTIONARY
    
    database ={'serkan': '1234', 'ali': '5678', 'ayse': '9012'}
username = input('Enter username: ')
password = input('Enter password: ')
if username not in database:
      print("The user does not exist")
elif database[username] == password:
      print("Congrats! You're logged in")
elif database[username] != password:
      print("Sorry - wrong combination")
