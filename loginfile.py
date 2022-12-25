import csv

def login():
    email = input("Enter user id : ")
    password = input("Enter password : ")
    with open("Users.csv",mode="r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if row == [email,password]:
                print("Login successfull")
                return True
    print("Please try again")
    return False
