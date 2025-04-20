from .display import *
from .key_commands import * 
from .keyboard_classes import *
from .key_creator import *
from .spell_checker import *

''''
A simple init that creates the actual tkinter mainloop and all systems

'''
#My master using my class to create the tkinter.Tk() 
master = BaseClass()

header_label = LabelClass(master, "Interactive Keyboard", expand=False)

'''
Just to find the key name, couldn't find a list in the docs
'''
# def key_press(event):
#     key= event.char
#     print(event)
#     print(f'{key}')
# master.bind("<Key>", key_press)


#Autocomplete - See details in file
def check_auto_complete() -> None:
    key_commands.check_auto_correct(master)
    master.after(60, check_auto_complete)


#Refreshes display2(text_box) every 20secs
def run_keyboard() -> None:
    display.set_text(displays[2])
    master.after(20, run_keyboard)

'''
Checks the state of the keyboard every 20secs
this is to bypass any issues if caps-lock is spammed/triggered oddly.
Whatever state the current keyboard is set to, is what the screens keys will be set to
- May allow it to bypass if no-keyboard, since you cant spam the button fast enough
'''  

def check_keyboard_caps() -> None:
    key_commands.caps_lock_key()
    master.after(20, check_keyboard_caps)

displays: list[FrameClass] = display.run(master)
#list[box_frame,receive_box,text_box]

#Creates the keys (See logic in file)
key_creator.run(master)

#Sets commands (See logic in file), passing in the display screen
key_commands.run(master, displays[0])