#password_manager.py
#store and display passwords for users
#Sam Hurd, Feb 22


user_list = ["bdsc", "pass1234"]


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
  