#password_manager.py
#store and display passwords for users
#Sam Hurd, Feb 22

name = ""
age = ""

password_list = []

user_list = ["bdsc", "pass1234"]




def menu(name, age):
    
    print("Hello {}".format(name))

    if age < 13:
        print("Sorry, you are not old enough to use the Password Manager. The programme will now exit")
        exit()

    else:
        option = input("Please choose a mode by entering a number from 1 to 3: \n 1. Add a password 2. View your passwords 3. Exit \n")
        return option


print("Welcome to the password manager")


name = input("What is your name? ")
while True:
    try:
        age = float(input("What is your age? "))
        chosen_option = menu(name, age)
    
    except:
        print("Please enter a number")


while True:
    chosen_option = menu(name, age)

    if chosen_option == "1":
        #call add_password function
        print("test")

    elif chosen_option == "2":
        #Call view_passwords function
        print("test")

    elif chosen_option == "3":
        #End programme
        break

    else:
        print("That is not a valid option. Please enter a number from 1 to 3")


print("Goodbye")