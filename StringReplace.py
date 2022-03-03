
import re

str = "Hello <<UserName>>, How are you?"
name = input("Enter the user name : ")

if re.match("[A-Z]{1}[a-z]{2,}$", name):
    new_str = str.replace("<<UserName>>", name)
    print(new_str)
else:
    print("Enter a valid name")
