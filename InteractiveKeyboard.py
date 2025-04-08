import tkinter
from tkinter import RIDGE, BOTH, X, BOTTOM, LEFT, RIGHT, TOP, END, N, S, E, W

from Keyboard.KeyboardClassFile import BaseClass, ButtonClass, LabelClass

tk = tkinter.Tk()
root = BaseClass(tk)

header_label = LabelClass(tk, "Interactive Keyboard")


box_frame = tkinter.Frame(tk, bg="#3e3e5b")
box_frame.pack(fill=BOTH, side=TOP, padx=10, pady=10)

receive_box = LabelClass(box_frame, "Enter Text")
receive_box.label.config(
    fg="white",
    bg="#3e3e5b",
    width=48,
    wraplength=640,
    justify="left",
    height=3
    )

final_text = []


def clear_text_box(event=None):
    final_text.clear()
    current_text.clear()
    receive_box.label.config(text="")

clear_button = ButtonClass(box_frame, "Clear", command = clear_text_box, side=RIGHT, width=12, bg="#1f1f2e")

text_box = LabelClass(tk, "Press a key to see the output")
text_box.label.config(
    fg="white",
    bg="#1f1f2e",
    width=48,
    height=1
    )

#Exit button
exit_button = ButtonClass(tk,"Exit",tk.quit,side=BOTTOM,padx=5,pady=1,
                          fill = X, width = 10, bg = "#000000")
#Button Frames
button_frame = tkinter.Frame(tk, bg="#1f1f2e")
button_frame.pack(fill=BOTH, side=BOTTOM, padx=10, pady=10)

internal_frame_top = tkinter.Frame(button_frame, bg="#1f1f2e")
internal_frame_top.pack(fill=BOTH, side=TOP)
internal_frame_midd = tkinter.Frame(button_frame, bg="#1f1f2e")
internal_frame_midd.pack(fill=BOTH)
lowest_internal = tkinter.Frame(button_frame, bg="#1f1f2e")
lowest_internal.pack(fill=BOTH, side=BOTTOM)
internal_frame_bot = tkinter.Frame(button_frame, bg="#1f1f2e")
internal_frame_bot.pack(fill=BOTH, side=BOTTOM)


#In order of QWERTY keyboard
buttons = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
button_nodes = []
button_counter = 0
current_text = []

def button_invoke(key):
    current_text.append(key)

def caps_lock_key(event=None):
    for each_button in button_nodes:
        current_text = each_button.button.cget("text")
        if current_text.isupper():
            each_button.button.config(text=current_text.lower())
        else:    
            each_button.button.config(text=current_text.upper())

def create_special_buttons():
    tab_key = ButtonClass(internal_frame_top, "Tab", lambda: button_invoke("\t"),side=LEFT, padx=4, pady=4, width=9, height=1)
    caps_lock = ButtonClass(internal_frame_midd, "Caps\nLock", command= caps_lock_key,side=LEFT, padx=4, pady=4, wraplength=26*6, height=1, width=10)
    shift_key = ButtonClass(internal_frame_bot, "Shift", lambda: print("Shift key pressed"), side=LEFT, padx=4, pady=4, width=12,height=1)
    tk.bind("<Tab>", lambda event: button_invoke("\t"))
    tk.bind("<Caps_Lock>", caps_lock.invoke_button)
    tk.bind("<Shift_L>", shift_key.invoke_button)


def erase(event):
    if len(current_text) > 0:
        current_text.pop(-1)
tk.bind("<BackSpace>", erase)

def enter_key(event=None):
    if len(current_text) >0:
        final_text.append("".join(current_text[:32]) + " ")
        receive_box.label.config(text="".join(final_text))
        current_text.clear()

tk.bind("<Return>", enter_key)
tk.bind("<space>", enter_key)


# def space_bar(event):
#     current_text.append(" ")

# Find keyname. ktyxbai
# def key_press(event):
#     key= event.char
#     print(event)
#     print(f'{key}')
# tk.bind("<Key>", key_press)

create_special_buttons()


def create_button(button, location):
    match(location):
        case "top":
            new_button = ButtonClass(internal_frame_top, button.lower(), command = lambda: button_invoke(new_button.button.cget("text")),
                                     side=LEFT, padx=5, pady=5, width=5)
            #Enables the button to be pressed with the keyboard
            tk.bind("<"+ button.lower() + ">", lambda event: button_invoke(button.lower()))
            tk.bind("<"+ button.upper() + ">", lambda event: button_invoke(button.upper()))
        case "mid":
            new_button = ButtonClass(internal_frame_midd, button.lower(), command = lambda: button_invoke(new_button.button.cget("text")),
                                     side=LEFT,padx=5, pady=5, width=5)
            tk.bind("<"+ button.lower() + ">", lambda event: button_invoke(button.lower()))
            tk.bind("<"+ button.upper() + ">", lambda event: button_invoke(button.upper()))
        case "bot":
            new_button = ButtonClass(internal_frame_bot, button.lower(), command = lambda: button_invoke(new_button.button.cget("text")),
                                     side=LEFT,padx=5, pady=5, width=5)
            tk.bind("<"+ button.lower() + ">", lambda event: button_invoke(button.lower()))
            tk.bind("<"+ button.upper() + ">", lambda event: button_invoke(button.upper()))
        case default:
            print("Failed")
    button_nodes.append(new_button)

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

def create_bottom_buttons():
    ctrl_key = ButtonClass(lowest_internal, "Ctrl", lambda: print("Alt key pressed"),side=LEFT, padx=4, pady=4, width=9,height=1)
    alt_key = ButtonClass(lowest_internal, "Alt", lambda: print("Alt key pressed"),side=LEFT, padx=4, pady=4, height=1, width=10)
    space_bar = ButtonClass(lowest_internal, "Space", command = enter_key, side=LEFT, padx=4, pady=4, width=32,height=1)


create_bottom_buttons()




def set_text():
    if len(current_text) <= 32:
        text_box.label.config(text="")
        text_box.label.config(text="".join(current_text))
        tk.after(20, set_text)
    else:
        tk.after(20, set_text)

set_text()


tk.mainloop()