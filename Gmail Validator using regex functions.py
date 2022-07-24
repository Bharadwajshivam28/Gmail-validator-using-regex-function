import re
gmail_condition = "^[a-z]+[a-z 0-9]+[\._]?[@]\w+[.]\w{2,3}$"
enter_gmail = input("Enter your Gmail : ")

if re.search(gmail_condition,enter_gmail):
    print("Right Gmail !")
else:
    print("Wrong Gmail !")