import tkinter
from tkinter.constants import *
#Separate file that holds classes
from KeyboardClassFile import BaseClass, ButtonClass, LabelClass, FrameClass
import KeyCommands
import Display
import KeyCreator

tk = tkinter.Tk()
root = BaseClass(tk)
header_label = LabelClass(tk, "Interactive Keyboard")

#Special Key Functions
# Find keyname. ktyxbai
def key_press(event):
    key= event.char
    print(event)
    print(f'{key}')
tk.bind("<Key>", key_press)

if __name__ =="__main__":
    displays = Display.run(tk)
    #[box_frame,receive_box,text_box]
    exit_button = ButtonClass(master = tk,text = "Exit",command = tk.quit,side=BOTTOM, fill = X,bg = "#000000")

    KeyCreator.run(tk)
    KeyCommands.run(tk, displays[0])

    def run_keyboard() -> None:
        Display.set_text(displays[2])
        tk.after(20, run_keyboard)
    
    def check_keyboard_caps() -> None:
        KeyCommands.caps_lock_key()
        tk.after(20, check_keyboard_caps)

    run_keyboard()
    check_keyboard_caps()
    tk.mainloop()