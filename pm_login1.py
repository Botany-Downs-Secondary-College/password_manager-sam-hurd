#password_manager.py
#store and display passwords for users
#Sam Hurd, Feb 22


user_list = ["bdsc", "pass1234"]


#def option_1():
    
#def option_2():





print("Welcome to the Password Manager")
name = input("What is your name? ")
while True:
    try:
        age = float(input("What is your age? "))
        break
    
    except:
        print("Please enter a number")

print("Hello {}".format(name))

if age < 13:
    print("Sorry, you are not old enough to use the password manager. The programme will now exit")
    exit()


while True:
    member = input("Enter L to log in or N to create a new account \n")

    if member == "L":
        username = input("Enter your username ")
        password = input("Enter your password ")
        if username and password in user_list:
            print("Log in successful")
            break
        elif username and password not in user_list:
            print("That combination does not match any existing account")

    elif member == "N":
        username = input("Enter a username \n")
        while True:
            password = input("Enter a password. Your password must contain at least eight characters, one capital letter and one number.")

            if (any(passreqs.isupper() for passreqs in password)
                and any(passreqs.isdigit()) for passreqs in password and len(password) >= 8):
                    user_list.append(username, password)
                    print("Account successfully created")
                    print(user_list)
                    break


            else:
                print("Your password does not meet the requirements")

    else:
        print("That is not a valid option, Enter L to log in or N to create a new account")

while True:
    option = int(input("Please choose a mode by entering a number from 1 to 3: \n 1. Add a password 2. View your passwords 3. Exit \n"))

    if option == "1":
        option_1()

    elif option == "2":
        option_2()

    elif option == "3":
        print("Thanks for using Password Manager!")
        exit()

    else:
        print("That is not a valid option")
  