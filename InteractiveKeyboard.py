import tkinter
from tkinter.constants import *
#Separate file that holds classes
from KeyboardClassFile import BaseClass, ButtonClass, LabelClass, FrameClass
import KeyCommands
import Display
import KeyCreator

'''
"interactive keyboard"
Made to accept both key presses and button presses to be able to write on-screen
Will be integrating spell-check and predictive text
'''

tk = tkinter.Tk()
root = BaseClass(tk)
header_label = LabelClass(tk, "Interactive Keyboard", expand=False)

'''
Just to find the key name, couldn't find a list in the docs
'''
# def key_press(event):
#     key= event.char
#     print(event)
#     print(f'{key}')
# tk.bind("<Key>", key_press)


#Autocomplete - See details in file
def check_auto_complete() -> None:
    KeyCommands.check_auto_correct(tk)
    tk.after(20, check_auto_complete)

#Refreshes display2(text_box) every 20secs
def run_keyboard() -> None:
    Display.set_text(displays[2])
    tk.after(20, run_keyboard)


'''
Checks the state of the keyboard every 20secs
this is to bypass any issues if caps-lock is spammed/triggered oddly.
Whatever state the current keyboard is set to, is what the screens keys will be set to
- May allow it to bypass if no-keyboard, since you cant spam the button fast enough
'''  
def check_keyboard_caps() -> None:
    KeyCommands.caps_lock_key()
    tk.after(20, check_keyboard_caps)


if __name__ =="__main__":
    displays: list[FrameClass] = Display.run(tk)
    #list[box_frame,receive_box,text_box]

    exit_button = ButtonClass(master = tk,text = "Exit", anchor="s",
                              command = tk.quit,side = BOTTOM, fill = X,bg = "#000000",
                              expand=False)
    #Creates the keys (See logic in file)
    KeyCreator.run(tk)

    #Sets commands (See logic in file), passing in the display screen
    KeyCommands.run(tk, displays[0])

    #my 2 loops
    run_keyboard()
    check_keyboard_caps()
    check_auto_complete()

    #tkinters standard window-loop
    tk.mainloop()