import tkinter
from tkinter.constants import *
from KeyboardClassFile import ButtonClass, FrameClass
import KeyCommands
import pyautogui  # type: ignore



#holds the button nodes, so i can tinker with them later
button_nodes: list[tkinter.Button] = []
#Just to place the QWERTY keys in order
button_counter: int = 0


def create_frame(master: tkinter.Tk) -> list:
    main_keyboard_frame = FrameClass(master, side=BOTTOM)
    internal_frame_top = FrameClass(main_keyboard_frame)
    internal_frame_midd = FrameClass(main_keyboard_frame)
    internal_frame_bot = FrameClass(main_keyboard_frame)
    lowest_internal = FrameClass(main_keyboard_frame, expand=True)
    return [main_keyboard_frame, internal_frame_top, internal_frame_midd, internal_frame_bot,lowest_internal]

def create_special_buttons(frame_top, frame_mid, frame_bot) -> None:
    tab_key = ButtonClass(
        master = frame_top, text = "Tab",
        command =  lambda : KeyCommands.button_invoke(key = "\t"),
        side=LEFT,  width=9,   fill= BOTH)
    
    caps_lock = ButtonClass(
        master = frame_mid, text = "Caps\nLock",
        command = lambda: pyautogui.press('capslock'),
        side=LEFT,  width=10,  fill= BOTH, wraplength=164)
    
    

    shift_key = ButtonClass(
        master = frame_bot, text = "Shift", 
        command = lambda: print("Shift key pressed"),
        side=LEFT,  width=12,  fill= BOTH)
    
    back_space = ButtonClass(
        master = frame_top, text = "BackSpace",
        command = KeyCommands.erase,
        side=RIGHT, width=9, fill= BOTH)
    
    enter_key = ButtonClass(
        master = frame_mid,text =  "Enter",
        command = KeyCommands.enter,
        side=RIGHT, width=10,  fill= BOTH)
    
    shift_key_r = ButtonClass(
        master = frame_bot, text = "Shift", 
        command = lambda: print("Shift key pressed"),
        side=RIGHT, width=12,  fill= BOTH)

def create_button(button, location: str, tk, frame) -> None:
    match(location):
        case "top":
            new_button = ButtonClass(
                master = frame, text= button.lower(),
                command = lambda: KeyCommands.button_invoke(str(new_button)),
                side=LEFT, padx=5, pady=5, width=5, fill = BOTH
            )
        case "mid":
            new_button = ButtonClass(
                master = frame,  text= button.lower(),
                command = lambda: KeyCommands.button_invoke(str(new_button)),
                side=LEFT,padx=5, pady=5, width=5, fill = BOTH)
        case "bot":
            new_button = ButtonClass(
                master = frame, text = button.lower(),
                command = lambda: KeyCommands.button_invoke(str(new_button)),
                side=LEFT,padx=5, pady=5, width=5, fill = BOTH)
        case default:
            print("Failed")
            
    button_nodes.append(new_button)
    
#     bind_buttons(tk, new_button)

# def bind_buttons(tk, new_button):
#     tk.bind("<"+ str(new_button).lower() + ">", lambda event : KeyCommands.button_invoke(str(new_button).lower()))
#     tk.bind("<"+ str(new_button).upper() + ">", lambda event: KeyCommands.button_invoke(str(new_button).upper()))

def create_bottom_buttons(frame) -> None:
    ctrl_key = ButtonClass(
        master = frame, text = "Ctrl",  
        command = lambda: print("Ctrl key pressed"),
        side=LEFT, fill=BOTH)
    
    alt_key = ButtonClass(
        master = frame,text =  "Alt",
        command =  lambda: print("Alt key pressed"),
        side=LEFT, fill=BOTH)
    
    space_bar = ButtonClass(
        master = frame,text =  "Space",
        command = KeyCommands.enter,
        width=46, side=LEFT,fill=BOTH)

    alt_key_r = ButtonClass(
        master = frame,text =  "Alt",
        command =  lambda: print("Alt key pressed"),
        side=LEFT, fill=BOTH)
    
    windows_key= ButtonClass(
        master = frame,text =  "WndK",
        command = lambda: print("WinKey key pressed"),
        side=LEFT, fill=BOTH)
    
    ctrl_key_r  = ButtonClass(
        master = frame,text =  "Ctrl",
        command = lambda: print("Ctrl key pressed"),
        side=LEFT, fill=BOTH)

def create_keyboard_keys(master, frame_top, frame_mid, frame_bot) -> None:
    #In order of QWERTY keyboard
    buttons: list[str] = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G",
    "H","J","K","L","Z","X","C","V","B","N","M"]
    button_counter = 0
    for button in buttons:
        if button_counter <10:
            create_button(button, "top", master, frame_top)
            button_counter += 1
        elif button_counter <= 18:
            create_button(button, "mid", master, frame_mid)
            button_counter += 1
        else:
            create_button(button, "bot", master, frame_bot)
            button_counter += 1

def run(master):
    frames = create_frame(master)

    ''' -- Frames --
    0: main_keyboard_frame,
    1: internal_frame_top, 
    2: internal_frame_midd,
    3: internal_frame_bot,
    4: lowest_internal
    '''

    buttons = create_special_buttons(
        frame_top = frames[1],frame_mid= frames[2], frame_bot= frames[3])
    
    create_keyboard_keys(master, frame_top = frames[1],
                        frame_mid= frames[2], frame_bot= frames[3])
    create_bottom_buttons(frames[4])
