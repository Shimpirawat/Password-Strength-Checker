import re

password= input("Enter Your Password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not re.search("[A-Z]", password):
    print("Password must contain at least 1 uppercase letter.") 
elif not re.search("[a-z]", password):
    print("Password must contain at least 1 lowercase letter.") 
elif not re.search("[0-9]", password):
    print("Password must contain at least 1 number.")
else:
    print("Password is strong.")    