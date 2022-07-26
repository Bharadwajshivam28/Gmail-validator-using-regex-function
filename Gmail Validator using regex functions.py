import re #importing function
gmail_condition = "^[a-z]+[a-z 0-9]+[\._]?[@]\w+[.]\w{2,3}$" #all valid condition for correct gmail format
enter_gmail = input("Enter your Gmail : ") #enter your gmail for checking

if re.search(gmail_condition,enter_gmail): 
    print("Right Gmail !")
else:
    print("Wrong Gmail !")
