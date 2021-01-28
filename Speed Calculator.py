from time import perf_counter
from pyautogui import prompt, confirm, alert

results = []

while True:
    input("Start")
    start = perf_counter()
    msg = prompt("Type something", "Prompt")
    if msg == "quit":
        confirm(f"Your record is {max(results)} keys/m", "Record")
    seconds = perf_counter() - start*60
    speed = round(len(msg) / seconds)
    if speed < 3:
        alert(f"Your current speed is {speed} keys/m", "Your speed is not good")
    else:
        alert(f"Your current speed is {speed} keys/m", "Your speed is good")
    try:
        if speed > max(results):
            alert("And that's a new highscore", "Highscore")
    except ValueError:
        confirm("And that's a new highscore", "Highscore")
    results.append(len(msg) / seconds)
