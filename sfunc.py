#!/usr/bin/python env

# functions used in send-mail.py

import re

def matchEmail(email: str, server="gmail.com"):
    # check the connecting server and construct a regex
    if server == "gmail.com":
        mail = "[a-zA-Z0-9]+@gmail.com"
    elif server == "outlook.com":
        mail = "[a-zA-Z0-9]+@outlook.com"
    # search for a match 
    x = re.search(mail, email)
    # there is no match for any of the email
    if x == None:
        return False
    # there was a match for the email
    return True

