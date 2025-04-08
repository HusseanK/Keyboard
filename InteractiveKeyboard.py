import tkinter
from tkinter.constants import *
#Separate file that holds classes
from KeyboardClassFile import BaseClass, ButtonClass, LabelClass

tk = tkinter.Tk()
root = BaseClass(tk)
header_label = LabelClass(tk, "Interactive Keyboard")


#Functions to create everything
def clear_text_box(event=None) -> None:
    final_text.clear()
    current_text.clear()
    receive_box.label.config(text="")

def button_invoke(key: str):
    current_text.append(key)

def caps_lock_key(event=None)->None:
    for each_button in button_nodes:
        current_text = each_button.button.cget("text")
        if current_text.isupper():
            each_button.button.config(text=current_text.lower())
        else:    
            each_button.button.config(text=current_text.upper())

def create_special_buttons() -> None:
    tab_key = ButtonClass(internal_frame_top, "Tab", lambda: button_invoke("\t"),
side=LEFT,  width=9,   fill= BOTH)
    
    caps_lock = ButtonClass(internal_frame_midd, "Caps\nLock", command= caps_lock_key,
side=LEFT,  width=10,  fill= BOTH, wraplength=164)
    
    shift_key = ButtonClass(internal_frame_bot, "Shift", lambda: print("Shift key pressed"),
side=LEFT,  width=12,  fill= BOTH)
    
    back_space = ButtonClass(internal_frame_top, "BackSpace", command=erase,
side=RIGHT, width=9,   fill= BOTH)
    
    enter_key = ButtonClass(internal_frame_midd, "Enter", command=enter,
side=RIGHT, width=10,  fill= BOTH)
    
    shift_key_r = ButtonClass(internal_frame_bot, "Shift", lambda: print("Shift key pressed"),
side=RIGHT, width=12,  fill= BOTH)

def create_button(button:str, location: str) -> None:
    match(location):
        case "top":
            new_button = ButtonClass(internal_frame_top, button.lower(), command = lambda: button_invoke(new_button.button.cget("text")),
                                     side=LEFT, padx=5, pady=5, width=5, fill = BOTH)
            #Enables the button to be pressed with the keyboard
            tk.bind("<"+ button.lower() + ">", lambda event: button_invoke(button.lower()))
            tk.bind("<"+ button.upper() + ">", lambda event: button_invoke(button.upper()))
        case "mid":
            new_button = ButtonClass(internal_frame_midd, button.lower(), command = lambda: button_invoke(new_button.button.cget("text")),
                                     side=LEFT,padx=5, pady=5, width=5, fill = BOTH)
            tk.bind("<"+ button.lower() + ">", lambda event: button_invoke(button.lower()))
            tk.bind("<"+ button.upper() + ">", lambda event: button_invoke(button.upper()))
        case "bot":
            new_button = ButtonClass(internal_frame_bot, button.lower(), command = lambda: button_invoke(new_button.button.cget("text")),
                                     side=LEFT,padx=5, pady=5, width=5, fill = BOTH)
            tk.bind("<"+ button.lower() + ">", lambda event: button_invoke(button.lower()))
            tk.bind("<"+ button.upper() + ">", lambda event: button_invoke(button.upper()))
        case default:
            print("Failed")
    button_nodes.append(new_button)

def create_keyboard_keys(buttons:list[str]) -> None:
    button_counter = 0
    for button in buttons:
        if button_counter <10:
            create_button(button, "top")
            button_counter += 1
        elif button_counter <= 18:
            create_button(button, "mid")
            button_counter += 1
        else:
            create_button(button, "bot")
            button_counter += 1

def create_bottom_buttons() -> None:
    ctrl_key    = ButtonClass(lowest_internal, "Ctrl",  lambda: print("Ctrl key pressed"),   side=LEFT, fill=BOTH)
    alt_key     = ButtonClass(lowest_internal, "Alt",   lambda: print("Alt key pressed"),    side=LEFT, fill=BOTH)
    space_bar   = ButtonClass(lowest_internal, "Space", command=enter, width=46,              side=LEFT,fill=BOTH)
    alt_key_r   = ButtonClass(lowest_internal, "Alt",   lambda: print("Alt key pressed"),    side=LEFT, fill=BOTH)
    windows_key = ButtonClass(lowest_internal, "WndK",  lambda: print("WinKey key pressed"), side=LEFT, fill=BOTH)
    ctrl_key_r  = ButtonClass(lowest_internal, "Ctrl",  lambda: print("Ctrl key pressed"),   side=LEFT, fill=BOTH)


#In order of QWERTY keyboard
buttons: list[str] = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G",
"H","J","K","L","Z","X","C","V","B","N","M"]
#holds the button nodes, so i can tinker with them later
button_nodes: list[tkinter.Button] = []
#Just to place the QWERTY keys in order
button_counter: int = 0
#Just the current text and the result text
final_text: list[str] = []
current_text: list[str] = []

#Special Key Functions
def erase(event=None)-> None:
    if len(current_text) > 0:
        current_text.pop(-1)

def enter(event=None)-> None:
    if len(current_text) > 0 :
        final_text.append("".join(current_text[ :32 ]) + " ")
        receive_box.label.config(text = "".join(final_text))
        current_text.clear()

# Find keyname. ktyxbai
# def key_press(event):
#     key= event.char
#     print(event)
#     print(f'{key}')
# tk.bind("<Key>", key_press)


def key_bindings() -> None:
    tk.bind("<Tab>", lambda event: button_invoke("\t"))
    tk.bind("<Return>", enter)
    tk.bind("<space>", enter)
    tk.bind("<Caps_Lock>", caps_lock_key)
    tk.bind("<Shift_L>", caps_lock_key)
    tk.bind("<Shift_R>", caps_lock_key)
    tk.bind("<BackSpace>", erase)


if __name__ =="__main__":
    box_frame = tkinter.Frame(tk, bg="#3e3e5b")
    box_frame.pack(fill=BOTH, side=TOP, padx=5, pady=5, expand=True)

    clear_button = ButtonClass(box_frame, "Clear", side=RIGHT, command = clear_text_box, bg="#1f1f2e", expand=False)

    receive_box = LabelClass(box_frame, "Enter Text", side=TOP,fg="white",bg="#3e3e5b",wraplength=640)
    text_box = LabelClass(tk, "Press a key to see the output")
    text_box.label.config(fg="white",bg="#1f1f2e",)

    exit_button = ButtonClass(tk,"Exit",tk.quit,side=BOTTOM, fill = X,bg = "#000000")

    #Keyboard button frame
    button_frame = tkinter.Frame(tk, bg="#1f1f2e")
    button_frame.pack(fill=BOTH, side=BOTTOM, padx=5, pady=5)
    #3x Internal frames
    internal_frame_top = tkinter.Frame(button_frame, bg="#1f1f2e")
    internal_frame_top.pack(fill=BOTH)
    internal_frame_midd = tkinter.Frame(button_frame, bg="#1f1f2e")
    internal_frame_midd.pack(fill=BOTH)
    internal_frame_bot = tkinter.Frame(button_frame, bg="#1f1f2e")
    internal_frame_bot.pack(fill=BOTH)
    lowest_internal = tkinter.Frame(button_frame, bg="#1f1f2e")
    lowest_internal.pack(fill=BOTH, expand=True)

    create_special_buttons()
    create_keyboard_keys(buttons)
    create_bottom_buttons()
    key_bindings()

    #Loop that checks and refreshes the texbox
    def set_text() -> None:
        #Stopping at 32 chars 
        if len(current_text) <= 32:
            text_box.label.config(text="")
            text_box.label.config(text="".join(current_text))
            #Refresh after 20secs
            tk.after(20, set_text)
        else:
            tk.after(20, set_text)

    set_text()
    tk.mainloop()