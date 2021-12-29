from pynput import keyboard
import pyautogui



def on_activate_stop():
    print('Exiting...')
    exit()


def on_activate_sell():
    pyautogui.PAUSE = 0.04
    print('sell')
    x, y = 1370, 640
    step = 85
    pyautogui.moveTo(x, y)
    for row in range(4):
        for column in range(7):
            pyautogui.click(x+column*step, y+row*step, button='right', clicks=2)
    pyautogui.keyUp('`')
    pyautogui.keyUp('alt')


def on_activate_shiny_dust():
    pyautogui.PAUSE = 0.05
    print('shiny dust')
    gem_x, gem_y = pyautogui.position()
    pyautogui.click(x=100, y=750, button='right')
    pyautogui.click(x=gem_x, y=gem_y, button='right')
    pyautogui.click(x=200, y=400)
    pyautogui.click(x=550, y=820)
    pyautogui.click(x=540, y=800)
    pyautogui.click(x=700, y=700)
    pyautogui.click(x=gem_x, y=gem_y, button='right')
    pyautogui.keyUp('`')
    pyautogui.keyUp('ctrl')


with keyboard.GlobalHotKeys({
    '<alt>+<ctrl>+c': on_activate_stop,
    '<ctrl>+`': on_activate_shiny_dust,
    '<alt>+`': on_activate_sell
        }) as hotkey:
    hotkey.join()
