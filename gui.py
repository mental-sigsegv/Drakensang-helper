import tkinter as tk
import json
from tkinter import *


def set_opacity(value):
    # print(f'Opacity: {value}')
    value = value/100+0.1
    with open("settings.json", "r+") as jfile:
        settings = json.load(jfile)
        settings['opacity'] = value
        jfile.seek(0)
        json.dump(settings, jfile)
        jfile.truncate()
    root.attributes('-alpha', value)


def changeOnHover(button, colorOnHover, colorOnLeave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


if __name__ == "__main__":
    BG_COLOR = '#641e16'

    root = tk.Tk()
    root.title("Drakensang scripts")
    root.geometry("280x450")
    root.wm_geometry("-100+100")
    root.iconbitmap('./images/drakensang_logo.ico')
    root.configure(bg=BG_COLOR)
    root.lift()

    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    Grid.rowconfigure(root, 1, weight=1)

    opacity_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=lambda *args: set_opacity(opacity_scale.get()), bg=BG_COLOR)
    opacity_scale.grid(column=0, row=2, sticky="NSEW")

    with open("settings.json", "r") as jfile:
        settings = json.load(jfile)
        opacity_scale.set((settings["opacity"]-0.1)*100)

    quit_button = Button(root, text="Quit", command=root.destroy, bg=BG_COLOR, activebackground='#cd6155')
    quit_button.grid(column=0, row=0, sticky="NE")
    changeOnHover(quit_button, "#cd6155", BG_COLOR)

    root.mainloop()
