import Display
from KeyboardClassFile import ButtonClass
from tkinter.constants import *
from KeyCreator import button_nodes
import ctypes

def clear_text_box(event=None) -> None:
    Display.final_text.clear()
    Display.current_text.clear()
    Display.receive_box.label.config(text="")

def caps_lock_key(event=None)->None:
    #Both the physical Capslock key, as well as the button are bound to this func

    #The button uses Pyautogui to set off the keyboards Caps key
    #and then i use Ctypes to check the caps state
    #This ensures if that someone presses caps/button key too fast, it'll always be accurate
    if bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14)):
        if str(button_nodes[0]).islower():
            for each_button in button_nodes:
                current_text = str(each_button)
                each_button.config(text=current_text.upper())
    else:
        if str(button_nodes[0]).isupper():
            for each_button in button_nodes:
                current_text = str(each_button)
                each_button.config(text=current_text.lower())


def erase(event=None)-> None:
    if len(Display.current_text) > 0:
        Display.current_text.pop(-1)

def enter(event=None)-> None:
    if len(Display.current_text) > 0 :
        Display.final_text.append("".join(Display.current_text[ :32 ]) + " ")
        Display.receive_box.label.config(text = "".join(Display.final_text))
        Display.current_text.clear()

def button_invoke(key: str, event=None):
    Display.current_text.append(key)

def key_bindings(master) -> None:
    master.bind("<Tab>", lambda event: button_invoke("\t"))
    master.bind("<Return>", enter)
    master.bind("<space>", enter)


    master.bind("<Caps_Lock>", caps_lock_key)
    
    #Make a shift-version for this
    # master.bind("<Shift_L>", caps_lock_key)
    # master.bind("<Shift_R>", caps_lock_key)

    master.bind("<BackSpace>", erase)
    for new_button in button_nodes:
        master.bind("<"+ str(new_button).lower() + ">",
                     lambda event : button_invoke(str(new_button).lower()))
        master.bind("<"+ str(new_button).upper() + ">",
                     lambda event: button_invoke(str(new_button).upper()))


def run(tk, box_frame) -> None:
    key_bindings(tk)
    clear_button = ButtonClass(
        master = box_frame, text = "Clear",
        command =  clear_text_box,
        side=RIGHT, bg="#1f1f2e", expand=False)