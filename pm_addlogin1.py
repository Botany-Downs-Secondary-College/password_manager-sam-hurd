#password_manager.py
#store and display passwords for users
#Sam Hurd, Feb 22
i = 1

user_list = ["bdsc", "pass1234"]
login_list = ["bdsc", "bdsc1234"]

def add_login():
    while True:
        app = input("Enter the name of the app or service, or enter 'menu' to return to the menu \n").strip().lower()
        if app == "menu":
            break
        else:
            username = input("What username did you use for {}?\n".format(app))
            while True:
                password = input("What password did you use?\n")

                login_list.append([app, username, password])
                print("Login added successfully")
                break


    
#def view_login():






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


while i == 1:
    member = input("Enter L to log in or N to create a new account \n")

    if member == "L":
        username = input("Enter your username ")
        password = input("Enter your password ")
        if username and password in user_list:
            print("Log in successful")
            i += 1
        elif username and password not in user_list:
            print("That combination does not match any existing account")

    elif member == "N":
        username = input("Enter a username \n")
        user_list.append(username)
        while True:
            password = input("Enter a password. Your password must contain at least eight characters, one capital letter and one number\n")
          
            if (any(passreqs.isupper() for passreqs in password) and any(passreqs.isdigit() for passreqs in password) and len(password) >= 8):
                    user_list.append(password)
                    print("Account successfully created")
                    i += 1
                    break


            else:
                print("Your password does not meet the requirements")

    else:
        print("That is not a valid option, Enter L to log in or N to create a new account \n")

while True:
    
    option = input("Please choose a mode by entering a number from 1 to 3: \n 1. Add a password 2. View your passwords 3. Exit \n")

    if option == "1":
        add_login()

    elif option == "2":
        view_login()

    elif option == "3":
        print("Thanks for using Password Manager!")
        exit()

    else:
        print("That is not a valid option. Please enter a number from 1 to 3 \n")
  