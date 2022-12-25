
from loginfile import *
from foodlist import *
from deletefood import *

print("Welcome to Food Ordering System")
print("Use admin,1234 or user,1111")
print("1. Log in as Admin")
print("2. Log in as User")
login_input = int(input("Enter your choice: "))
if login_input == 1:
    login()
    print("1. Show food list")
    print("2. Delete item from food list by ID")
    print("3. Search food by ID")
    print("4. Add new food item")
    print("5. To exit")
    admin_input = int(input("Enter your choice: "))
    if admin_input == 1:
        showfood()
    elif admin_input == 2:
        fooddel()
    elif admin_input == 3:
        pass
    elif admin_input == 4:
        pass
    elif  admin_input == 5:
        pass
    else:
        print("wrong input")

elif login_input == 2:
    login()
else:
    print("Wrong input")