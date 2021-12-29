import tkinter as tk


opacity = 1
def makeSomething(value):
    global opacity
    opacity = value
    print(opacity)

root = tk.Tk()
root.title("Drakensang scripts")
root.geometry("280x450")
root.attributes('-alpha', opacity)

canvas = tk.Frame(root)
canvas.grid()

tk.Label(canvas, text="Hello World!").grid(column=0, row=0)
tk.Button(canvas, text="Quit", command=root.destroy).grid(column=1, row=0)
tk.Button(canvas, text="Opacity", command=lambda *args: makeSomething(0.6)).grid(column=1, row=0)

root.mainloop()
