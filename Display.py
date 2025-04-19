from KeyboardClassFile import LabelClass, FrameClass
from tkinter.constants import *

'''
Display, will end up fixing the way it does everything
Right now it just needs to work, no need to make things pretty
'''

final_text: list[str] = [] #Holds the text in the final window
current_text: list[str] = [] #Holds the text while typing, before submitting

#global variables means bad code - need to fix below, do before commit
receive_box = None

def run(master):
    global receive_box
    '''
    Creates my main display frame and sets everything up
    '''
    box_frame = FrameClass(master, bg="#3e3e5b",
                           fill=BOTH, side=TOP, padx=5, pady=5, expand=True)
    
    receive_box = LabelClass(box_frame, "Enter Text", side=TOP, expand=True,
                             anchor='s',fg="white",bg="#3e3e5b", 
                             wraplength=1400)
    
    
    text_box = LabelClass(master, "Press a key to see the output", 
                          fill = X, side=TOP, expand=False)
    text_box.label.config(fg="white",bg="#1f1f2e")


    return [box_frame,receive_box,text_box]


def set_text(text_box) -> None:
    '''
    just displays text, this runs every 20ms through the main file
    Stopping at 32 chars, because words SHOULDNT(3 do) extend past 32chars
    '''
    if len(current_text) <= 32:
        text_box.label.config(text="")
        text_box.label.config(text="".join(current_text))