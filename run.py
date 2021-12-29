import os

if __name__ == "__main__":
    with open("./script.py", "r") as script:  # start script
        exec(script.read())
        print("Script loaded\n")

    os.startfile("")
