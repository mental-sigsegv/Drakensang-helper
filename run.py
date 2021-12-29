import os

with open("./script.py", "r") as script:
    exec(script.read())
    print("Script loaded\n")