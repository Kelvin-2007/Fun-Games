from pyautogui import prompt, alert

mass = float(prompt("Please Input Your weight"))
alert(f"Your weight is {round(mass*9.81)}n,\nAnd your mass is {mass}kg,\nKnow the difference")