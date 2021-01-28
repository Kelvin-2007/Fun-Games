from pyautogui import alert, confirm, prompt
from pyperclip import copy
from random import choice, randint

action = confirm("Choose The Function", "Startup", ("Check", "Generate"))

signs = ["!", "@", "#", "-", "_"]

def upper(password: str) -> bool:
    upper = False
    for char in password:
        if char.isupper():
            upper = True
    return upper

def lower(password: str) -> bool:
    lower = False
    for char in password:
        if char.islower():
            lower = True
    return lower

def num(password: str) -> bool:
    numc = False
    for char in password:
        if char.isdigit():
            numc = True
    return numc

def sign(password: str) -> bool:
    global signs
    signc = False
    for char in password:
        if char in signs:
            signc = True
    return signc

def length(password: str) -> bool:
    return len(password) >= 6 and len(password) <= 16

def randomcase(x: str) -> str:
    rcs = list(x)
    for index in range(0, randint(0, len(x)-1)):
        if randint(0, 5) == randint(0, 5):
            rcs[index] = rcs[index].upper()
        else:
            rcs[index] = rcs[index].lower()
    return "".join(x)

def Generate(name: str, dob: str) -> str:
    password = randomcase(name)+choice(signs)+dob
    return password

if action == "Check":
    password = prompt("Please Type Your Password", "Password", "example@dob")
    fl = length(password)
    hasupper = upper(password)
    haslower = lower(password)
    hasnum = num(password)
    hassigns = sign(password)
    score = 0
    if hasupper:
        score += 1
    if haslower:
        score += 1
    if hasnum:
        score += 1
    if hassigns:
        score += 1
    alert(f"Your Password is {(score/4)*100}% strong", "Password Strength", timeout=10000)

else:
    name = prompt("Please Enter Your Name", "Generate Password")
    yob = prompt("Please Enter Your Year Of Birth", "Generate Password")
    password = Generate(name, yob)
    alert(f"Your Generated Password is {password}")
    clipboardper = confirm("Should I Copy That To Your Clipboard", "Generate Password", ("Yes", "No"))
    if clipboardper == "Yes":
        copy(password)